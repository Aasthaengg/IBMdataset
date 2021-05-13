#!/usr/bin/env python3
s=input()
k='keyence'
for i in range(8):
    if k[:i] == s[:i]:
        if k[-7+i:]==s[-7+i:] or i==7:
            print('YES')
            exit()
print('NO')
