# -*- coding: utf-8 -*-
#ARC102C
import sys

#n= int(input())
tmp = input().split()
n,k = list(map(lambda a: int(a), tmp))

if(k%2==1):
	tmp=n//k
	ans=tmp*tmp*tmp
else:
	tmp=n//k
	ans=tmp*tmp*tmp
	tmp=(n+k//2)//k
	ans+=tmp*tmp*tmp

print(ans)