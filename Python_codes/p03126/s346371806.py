#!/usr/bin/env python3

N,M = map(int,input().split())
lst = [i+1 for i in range(M)]


for _ in range(N):
    tmp = list(map(int,input().split()))
    K = tmp[0]
    A = tmp[1:]
    lst = list(filter(lambda x: x in A,lst))

print(len(lst))