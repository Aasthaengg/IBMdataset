#!/usr/bin/env python3
s=input()
print('GBoaodd'[any(s[i-1]==s[i]for i in range(1,len(s)))::2])
