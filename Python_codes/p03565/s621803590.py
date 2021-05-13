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
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque



def run():
    S = input()
    T = input()
    ref = 'abcdefghijklmnopqrstuvwxyz'
    ans =[]
    for i in range(len(S)-len(T)+1):
        checked = True
        for j in range(len(T)):
            if S[i+j] == T[j] or S[i+j]=='?':
                continue
            else:
                checked = False
                break
        if checked:
            ret = S[:i].replace('?', 'a') + T + S[i+len(T):].replace('?', 'a')
            ans.append(ret)
    try:
        print(sorted(ans)[0])
    except:
        print('UNRESTORABLE')



if __name__ == "__main__":
    run()
