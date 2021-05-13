#!/usr/bin/env python3
n = int(input())
a = input().split()
ans = a[0::2][::-1] + a[1::2]
if n % 2:
    print(*ans)
else:
    print(*ans[::-1])
