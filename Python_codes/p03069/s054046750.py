#!/usr/bin/env python3
n = int(input())
s = input()
w = s.count(".")
b = 0
ans = w
for i in s:
    b += i =="#"
    w -= i == "."
    ans = min(ans, w+b)
print(ans)
