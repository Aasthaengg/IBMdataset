#!/usr/bin/env python3
n, k = map(int, input().split())

okashi = [0] * n
for _ in range(k):
    d = int(input())
    for i in list(map(int, input().split())):
        okashi[i - 1] += 1

ans = 0
for i in okashi:
    if i == 0:
        ans += 1

print(ans)

