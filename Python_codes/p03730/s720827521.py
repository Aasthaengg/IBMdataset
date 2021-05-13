#!/usr/bin/env python3
a, b, c = map(int, input().split())

st = a % b

for i in range(2, b + 1):
    ans = a * i % b

    if ans == c:
        print("YES")
        exit()
    elif ans == st:
        print("NO")
        exit()