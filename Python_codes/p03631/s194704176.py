# -*- coding: utf-8 -*-
import sys

#----------
s = input().strip()
#----------
for i in range(len(s)//2+1):
    if s[i] != s[len(s)-1-i]:
        print("No")
        sys.exit()

print("Yes")
