#!/usr/bin/env python3
N = int(input())
a = [int(input()) for i in range(N)]

x = 1
ans = 0
for i in range(N):
    ans += 1
    x = a[x - 1]
    if x == 2:
        print(ans)
        exit()
print(-1)
