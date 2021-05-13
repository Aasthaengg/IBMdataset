#!/usr/bin/env python3
s = input()
c_bit = 0
for i in range(len(s)):
    if c_bit and s[i] == "F":
        print("Yes")
        exit()
    if s[i] == "C":
        c_bit = 1
print("No")