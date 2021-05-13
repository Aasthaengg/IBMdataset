#!/usr/bin/env python
N = int(input())
A = list(map(int, input().split()))
ans = 0
s = 0
j = 0

for i in range(N):
    while j < N and not (s & A[j]):
        s ^= A[j]
        j += 1
    ans += j-i
    s ^= A[i]
print(ans)
