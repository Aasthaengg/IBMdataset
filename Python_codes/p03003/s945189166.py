#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,m=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
arr=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if S[i] == T[j]:
            arr[i][j] = 1
acum = [[0]*m for i in range(n)]
acum[0][0] = arr[0][0]
for i in range(1,n):
    acum[i][0] = acum[i-1][0] + arr[i][0]
for j in range(1,m):
    acum[0][j] = acum[0][j-1] + arr[0][j]
for i in range(1,n):
    for j in range(1,m):
        arr[i][j] += (acum[i-1][j-1])*(arr[i][j])
        acum[i][j] = acum[i-1][j] + acum[i][j-1] - acum[i-1][j-1] + arr[i][j]
        arr[i][j] %= mod; acum[i][j] %= mod
print(1+sum(map(sum,arr))%mod)
# print(*arr,sep="\n");print()
# print(*acum,sep="\n")


