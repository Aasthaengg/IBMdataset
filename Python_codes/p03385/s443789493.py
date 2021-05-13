import sys
import math

#a,b,c = map(int, input().split())
s = input()
li = [''] * 3
for i in range(3):
    li[i] = s[i]
li.sort()
li2 = ['a', 'b', 'c']
if (li == li2):
    print('Yes')
else:
    print('No')