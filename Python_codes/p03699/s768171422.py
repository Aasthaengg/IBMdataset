#!/usr/bin/env python3

n = int(input())
s = [int(input()) for _ in range(n)]
s = sorted(s)

ans = sum(s)
if ans%10 != 0:
    print(ans)
    exit(0)
    
for i in s:
    if i%10 != 0:
        ans -= i
        print(ans)
        exit(0)

print(0)
