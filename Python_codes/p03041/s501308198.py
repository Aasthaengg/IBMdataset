#!/usr/bin/env python3

N, K = map(int, input().split())
S = input()
cnt = 0
ans = ""

for i in S:
    if cnt == K-1:
        ans += i.swapcase()
    else:
        ans += i
    cnt += 1

print(ans)