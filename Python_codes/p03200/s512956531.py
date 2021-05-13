#!/usr/bin/env python3
s=input()
c=0
a=0
for i in s:
    if i =="W":
        a += c
    else:
        c += 1
print(a)
