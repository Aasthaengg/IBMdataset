# coding: utf-8
import sys

s = input()

if len(s) < 4:
    print("No")
    sys.exit()
if s[0]=='Y' and s[1]=='A' and s[2] == 'K' and s[3] == 'I':
    print("Yes")
else:
    print("No")
