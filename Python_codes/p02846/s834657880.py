#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect, string, copy
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
mod = 10**9+7
ans = count = 0; pro = 1

t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
if a1>b1:
    a1,b1=b1,a1
    a2,b2=b2,a2
if a1*t1+a2*t2<b1*t1+b2*t2:
    print(0)
    exit()
elif a1*t1+a2*t2 == b1*t1+b2*t2:
    print("infinity")
    exit()
dis=t2*(a2-b2)+t1*(a1-b1)
ans=(t1*(b1-a1))//dis
anssub = (t1*(b1-a1))%dis
if anssub==0:
    sub=0
else:
    sub=1
print(ans*2+sub)
