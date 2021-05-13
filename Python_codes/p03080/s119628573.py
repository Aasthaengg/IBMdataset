# -*- coding: utf-8 -*-

N = int(input())
s = input()

s = s.replace("B", "")

if len(s) > N - len(s):
    print("Yes")
else:
    print("No")
