# coding: utf-8
# Your code here!
# 5
# 14
# ITP1_3_D

count=0
a,b,c=map(int,input().split())
for i in range(a,b+1):
    if c%i==0:
        count=count+1
print(count)
