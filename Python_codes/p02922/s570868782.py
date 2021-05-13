#!/usr/bin/env python3

A, B = [int(x) for x in input().split(" ")]

ans = 0
kazu = 1
while B > kazu:
    ans += 1
    kazu = kazu - 1 + A

print(ans)
    

