from __future__ import print_function
# import numpy as np
# import numpypy as np
import sys
input = sys.stdin.readline

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return

import math
import string
import fractions
from fractions import Fraction
from fractions import gcd

def lcm(n,m):
    return int(n*m/gcd(n,m))

import re
import array
import copy
import functools
import operator

import collections
import itertools
import bisect
import heapq


from heapq import heappush
from heapq import heappop
from heapq import heappushpop
from heapq import heapify
from heapq import heapreplace

from queue import PriorityQueue as pq

def reduce(p, q):
    common = fractions.gcd(p, q)
    return (p//common , q//common )
# from itertools import accumulate
# from collections import deque

import random

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):       # 2つのデータxとyが同じ木に属するならtrue，そうでなければfalseを返す
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    
def main():
    n_len_of_seq, m_num_of_pairs = map(int, input().split())
    union_find_forest = UnionFind(n_len_of_seq) # 数列の長さだけの木からなるunion_find森を作る
    p_seq  = list(map(int, input().split()))
    p_seq = [p_seq[i] - 1 for i in range(len(p_seq))]

    # eprint("union_find_forest")
    # eprint(union_find_forest)
    # eprint()

    for index in range(m_num_of_pairs): # loop for each element (pair) in pairs
        x_pair,y_pair = map(int, input().split())
        x_pair-=1
        y_pair-=1
        union_find_forest.union( x_pair , y_pair) # x_pair-1の木とy_pair-1の木を併合する
        # eprint(union_find_forest)
        # eprint()
        
    cnt=0
    for i in range(n_len_of_seq): # loop for p_seq (sequence of integeres)
        if union_find_forest.same(i, p_seq[i]): # 例えばp_seqのindex==3であるところ(p_seqの4番目)(値は4であって欲しい)について，うにふぁい森の中で4とp_seq[3](の値)が同じ木に属していれば，それらを交換できる(何回でもペア交換は適用できるからね)(連結成分のなかは自由自在に入れ替えられる)．
            # やっぱバグるので全部 0 based index に直しました
            cnt+=1
    
    print(cnt)
    # p_seq = list(map(int, input().split()))
    # pairs=[[0,0] for _ in range(m_num_of_pairs)]
    # # eprint(pairs)
    # for index_pairs in range(m_num_of_pairs):
    #     pairs[index_pairs][0] , pairs[index_pairs][1] = map(int, input().split())
    #     # eprint(index_pairs)
    #     # eprint(pairs[index_pairs])
    #     # eprint(pairs)
    # eprint(pairs)

    
    return

if __name__ == '__main__':
    main()
