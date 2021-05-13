#!/usr/bin/env python3

N = int(input())
D,X = [int(i) for i in input().split()]
A = [int(input()) for _ in range(N)]

X += N
for d in range(2,D+1):
    for a in A:
        if (d - 1) % a == 0:
            X += 1

print(X)
