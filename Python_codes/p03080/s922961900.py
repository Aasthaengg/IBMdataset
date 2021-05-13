# coding: utf-8

N = int(input())
s = input()
R, B = [], []

for i in range(len(s)):
    if s[i] == 'R':
        R.append(s[i])
    else:
        B.append(s[i])
if len(R) > len(B):
    print('Yes')
else:
    print('No')
