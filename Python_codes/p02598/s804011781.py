# -*- coding: utf-8 -*-
import sys
N,K=map(int, sys.stdin.readline().split())
A=map(int, sys.stdin.readline().split())

#最大の長さがnの丸太にK回切ってすることができるか？
def func(n):
    cnt=0
    for a in A:
        #print "a :: ",a
        if a%n==0:
            cnt+=a/n-1
        else:
            cnt+=a/n
    if cnt<=K:
        return True
    else:
        return False

l=0
r=10**9
while 1<r-l:
    m=(l+r)/2
    if func(m):
        r=m
    else:
        l=m
print r