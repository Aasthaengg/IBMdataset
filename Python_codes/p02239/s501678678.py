# -*- coding: utf-8 -*-
'''
所要時間は、分位であった。
'''


# ライブラリのインポート
#import re #正規表現
import sys
#import heapq
#import bisect
from collections import deque
#import math

def main():
    inf = 10000
    n = int(input())
    D = [inf for i in range(n)]
    L = [[] for i in range(n)]
    for i, line in enumerate(sys.stdin):
        L[i] = list(map(lambda x: int(x)-1, list(line.strip("\n").split())))

    q = deque([0])
    D[0] = 0
    while(len(q)):
        u = q.popleft()
        if L[u][1] == -1:
            continue
        for j in range(2,len(L[u])):
            if D[L[u][j]] == inf:
                q.append(L[u][j])
            D[L[u][j]] = min(D[L[u][0]] + 1, D[L[u][j]]) 

                      
    for i in range(n):
        print("{} {}".format(i+1,D[i])) if D[i] < inf else print("{} {}".format(i+1,-1))
            
if __name__ == '__main__':
    main()

