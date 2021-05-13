#!/usr/bin/python3

n = int(input())
s = input()
cr = sum([int(c == 'R') for c in s])
cb = n - cr
if cr > cb:
    print("Yes")
else:
    print("No")
