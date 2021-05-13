# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n = int(input())
a = [int(i) for i in readline().split()]
a = [c-(i+1) for i,c in enumerate(a)]

a.sort()
m = a[n//2]

print(sum(abs(i-m) for i in a))