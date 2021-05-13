# -*- coding: utf-8 -*-

N = int(input())
D, X = map(int, input().split())

ans = 0

for i in range(N):
    Ai = int(input())
    for j in range(1, D + 1, Ai):
        ans += 1

ans += X

print(ans)
