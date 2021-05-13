# coding: utf-8
k, t = map(int,input().split())
A=list(map(int,input().split()))
m=max(A)
s=k-m
print(max(m-1-s, 0))