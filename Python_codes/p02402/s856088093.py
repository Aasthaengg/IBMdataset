#coding:utf-8
import sys
n=int(input())
a=map(int,input().split())

min,max,sum=2**63-1,-2**63,0

for i in a:
    if i<min:
        min=i
    if max<i:
        max=i
    sum+=i

print(str(min)+" "+str(max)+" "+str(sum))