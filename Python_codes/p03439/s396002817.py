# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7
def intread():
    return int(sysread())
def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())


def get_ideal(s, target, s_val, N):
    dic = {'Male' : 0, 'Female' :1}
    rev = {0 : 'Male', 1: 'Female'}
    dist = min([abs(target - s), s + N - target, target + N - s])
    v = (dic[s_val] + (dist % 2)) % 2
    #print(s, target, s_val, rev[v])
    return rev[v]

def check(v):
    return True if v == 'Vacant' else False

from time import sleep
def query(x, L):
    print(x)
    #print('query: ', x)
    #print('')
    #sleep(1)
    v = input()
    #sleep(1)
    L[x] = v
    if check(v):
        #printout('end')
        #sprint()
        return True



def run():
    N = int(input())
    L = [''] * N
    check_lists = deque([])

    if query(0, L): return
    if query(N-1, L): return

    check_lists.append((0, N-1))
    while check_lists:
        #print(check_lists)
        a, b = check_lists.popleft()
        if abs(a-b) == 1:continue
        x = (a + b) // 2

        if query(x, L): return
        pred_a = get_ideal(a, x, L[a], N)
        pred_b = get_ideal(b, x, L[b], N)
        #print(pred_a, pred_b)
        if pred_a == pred_b == L[x]:
            check_lists.append((a, x))
            check_lists.append((x, b))
        elif pred_a != L[x]:
            check_lists = deque([])
            check_lists.append((a, x))
        elif pred_b != L[x]:
            check_lists = deque([])
            check_lists.append((x, b))

if __name__ == "__main__":
    run()
