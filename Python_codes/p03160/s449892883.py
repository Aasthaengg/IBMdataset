#!/usr/bin/env python3

n = int(input())

harr = [int(i) for i in input().split(' ')]

twojump = 0
onejump = abs(harr[1] - harr[0])
ans = onejump

for i in range(2, n):
    ans = min(abs(harr[i]-harr[i-1])+onejump, abs(harr[i]-harr[i-2])+twojump)
    twojump = onejump
    onejump = ans

print(ans)
