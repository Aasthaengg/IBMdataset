#!/usr/bin/env python3
S = input()

s = ''
for i in range(len(S)):
    if S[i] in s:
        print('no')
        exit()
    else:
        s += S[i]
print('yes')
