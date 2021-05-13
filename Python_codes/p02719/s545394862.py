# coding: utf-8
# Your code here!

N,K=map(int,input().split())
a=N%K

if K-a<=a:
    print(K-a)
else:
    print(a)