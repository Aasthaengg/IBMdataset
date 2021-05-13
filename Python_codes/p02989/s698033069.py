#!/usr/bin/ python3.8
N=int(input())
d=[int(x) for x in input().split()]
d=sorted(d)

if N%2==1:
    print(0)
    exit(0)

print(d[N//2] - d[N//2-1])
