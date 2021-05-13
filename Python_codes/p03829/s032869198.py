# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n,a,b = [int(i) for i in readline().split()]
x = [int(i) for i in readline().split()]

walk = [xj-xi for xi,xj in zip(x,x[1:]) if a*(xj-xi) < b]

w = sum(walk)*a
t = (n-1-len(walk))*b

print(t+w)
