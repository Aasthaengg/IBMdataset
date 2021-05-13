#!/usr/bin/env python3
s = input()
for i in range(3):
    if s[i] == s[i+1]:
        print("Bad")
        s = 0
        break
if s != 0:
    print("Good")