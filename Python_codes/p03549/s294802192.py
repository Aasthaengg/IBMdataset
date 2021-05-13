#!/usr/bin/env python3

N, M = map(int, input().split())

ms = 1900
ans = 2**M * ms * M
ans += ((N-M)*100)*2**M
print(ans)
