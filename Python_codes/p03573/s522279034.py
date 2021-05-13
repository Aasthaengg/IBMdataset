# coding: utf-8
import math
a, b, c = map(int,input().split())
#N = int(input())
#S = input()
ans = 0
#l = list(map(int,input().split()))

l = [a,b,c]

if l.count(a) == 1:
    print(a)
elif l.count(b) == 1:
    print(b)
else:
    print(c)