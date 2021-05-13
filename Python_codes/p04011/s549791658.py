# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
x = int(input())
y = int(input())

if k<=n:
  print(k*x+(n-k)*y)
else:
  print(n*x)