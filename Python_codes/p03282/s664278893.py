#!/usr/bin/env python3
s = input()
k = int(input())

i = 0
while i < len(s) - 1:
    if i == k - 1:
        print(s[i])
        exit()
    if s[i] == "1":
        i += 1
    else:
        print(s[i])
        exit()
print(s[i])
