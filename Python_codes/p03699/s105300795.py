#!/usr/bin/env python3

N = int(input())
S = sorted([int(input()) for i in range(N)])
ans = sum(S)

if ans % 10 == 0:
    for i in S:
        if (ans - i) % 10 != 0:
            ans -= i
            break

if ans % 10 == 0:
    ans = 0

print(ans)



