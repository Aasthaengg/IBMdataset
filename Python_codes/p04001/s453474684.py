# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

#n,*p = map(int, read().split())


s = input()

L = len(s)
ans = 0
from itertools import product
for a in product(["+",""],repeat=L-1):
    t = s[0]
    for si,i in zip(s[1:],a):
        t += i + si
        
    #print(t)
    ans += eval(t)

print(ans)

