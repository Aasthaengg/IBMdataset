# -*- coding: utf-8 -*-
#"""
#Created on Wed Nov 20 17:37:14 2019
#
#@author: manakamura
#"""

#https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_c

n= int(input())
#s= input()
tup = []
for i in range(0,n):
    tmp = input().split()
    tmpa,tmpb = list(map(lambda a: int(a), tmp))
    tup.append([tmpa+tmpb,tmpa,tmpb])

#print(tup)
tup=sorted(tup, reverse=True, key=lambda x:x[0])
#print(tup)

total=0
for i in range(0,n):
    if (i%2==0):
       total+=tup[i][1]
    else:
       total-=tup[i][2]
          
print(total)