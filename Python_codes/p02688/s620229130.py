#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int, input().split())
s=[[0] * k for i in range(n)]
for i in range(k):
  input()
  l=list(map(int, input().split()))
  for j in range(len(l)):
    s[l[j]-1][i]=1

r=0
for i in range(n):
  if sum(s[i])==0:
    r=r+1
print(r)
