#!/usr/bin/env python3
n, Q = map(int, input().split())
s = input()
q = [[*map(int, input().split())] for _ in range(Q)]
R = [0]
for i in range(n - 1):
    R.append(R[-1] + (s[i:i + 2] == "AC"))
for l, r in q:
    print(R[r-1]-R[l-1])
