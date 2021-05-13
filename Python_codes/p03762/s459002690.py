# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意


#n = int(input())
n,m = [int(i) for i in readline().split()]
x = [int(i) for i in readline().split()]
y = [int(i) for i in readline().split()]

MOD = 10**9+7

si = 0
for i in range(n-1):
    si += (x[i+1]-x[i])*(i+1)*(n-i-1)
    si %= MOD

sj = 0
for j in range(m-1):
    sj += (y[j+1]-y[j])*(j+1)*(m-j-1)
    sj %= MOD


#print(si,sj)

print(si*sj%MOD)