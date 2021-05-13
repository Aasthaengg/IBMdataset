#coding: utf-8

S = input()

ret  = 0
numW = 0
for c in reversed(S):
    if c == 'B':
        ret += numW
    else:
        numW+=1

print(ret)
