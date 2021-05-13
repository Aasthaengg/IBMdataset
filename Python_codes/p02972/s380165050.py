#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
a = [0, *(int(x) for x in input().split())]
divisors = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        divisors[j].append(i)
ans = []
for i in reversed(range(1, n + 1)):
    if a[i]:
        for j in divisors[i]:
            a[j] ^= 1
        ans.append(i)
print(len(ans))
print(*ans)
