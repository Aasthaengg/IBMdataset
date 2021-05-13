# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque

INF = 1 << 50

def create_new_arr(DICT, SEQ):
    new_seq = ''
    next_id = 0
    for s in SEQ:
        if s not in DICT:
            DICT[s] = str(next_id)
            next_id += 1
        new_seq += DICT[s]
    return new_seq

def run():
    S, T = input(), input()
    s_dic = {}
    t_dic = {}

    new_S = create_new_arr(s_dic, S)
    new_T = create_new_arr(t_dic, T)

    if new_S == new_T:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    run()