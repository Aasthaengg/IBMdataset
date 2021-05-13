#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	G_fix
# CreatedDate:  2020-06-05 21:28:41 +0900
# LastModified: 2020-06-05 22:05:41 +0900
#


import os
import sys
from collections import deque
#import numpy as np
#import pandas as pd


def main():
    n,m = map(int,input().split())
    path = [[] for _ in range(n+1)]
    to_cnt = [0]*(n+1)
    longest_cnt = [0]*(n+1)
    for _ in range(m):
        x,y = map(int,input().split())
        path[x].append(y)
        to_cnt[y]+=1
    
    Q = deque()
    for i in range(1,n+1):
        if to_cnt[i]==0:
            Q.append(i)

#    longest_cnt[s]=1

    while(Q):
        u = Q.popleft()
        for v in path[u]:
            to_cnt[v]-=1
            if longest_cnt[u]+1>longest_cnt[v]:
                longest_cnt[v]=longest_cnt[u]+1
            if to_cnt[v]==0:
                Q.append(v)
    print(max(longest_cnt))



if __name__ == "__main__":
    main()
