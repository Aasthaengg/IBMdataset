# -*- Coding: utf-8 -*-

n, m = (int(i) for i in input().split())

t = (1900*m+100*(n-m))*2**m

print(t)