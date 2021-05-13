#import decimal
#decimal.getcontext().prec==500 Floatの桁数を500まで増やす
#Decimal(c).sqrt() それで平方根を求める
#Decimal(1) / Decimal(7) 1/7

from collections import *
from itertools import *
from bisect import *
from heapq import *
import copy
import math
from fractions import gcd
import sys
#input = sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))

data=[]
for i,a in enumerate([2,5,5,4,5,6,3,7,6]):
    if i+1 in A:
        data.append([a,i+1])

dic={}
for a,i in reversed(data):
    dic[i]=0
dp=[copy.copy(dic) for i in range(N+1)]

def main(dic1,dic2):
    dic1=sorted([[str(i),dic1[i]] for i in dic],key=lambda x:x[0],reverse=True)
    dic2=sorted([[str(i),dic2[i]] for i in dic],key=lambda x:x[0],reverse=True)
    for a,b in zip(dic1,dic2):
        if a[1]>b[1]:
            return(0)
        if a[1]<b[1]:
            return(1)
    return(0)

def _sum(dic):
    count=0
    for i in dic:
        count+=dic[i]
    return(count)


for a,n in data:
    tempdic=copy.copy(dic)
    tempdic[n]+=1
    if len(dp)-1>=a:
        flag=main(dp[a],tempdic)
        if flag:
            dp[a]=tempdic
    for i in range(len(dp)):
        if i>=a and _sum(dp[i-a]):
            if _sum(dp[i])<_sum(dp[i-a])+1:

                tempdic=copy.copy(dp[i-a])
                tempdic[n]+=1
                dp[i]=tempdic
            elif _sum(dp[i])==_sum(dp[i-a])+1:
                dp[i-a][n]+=1
                flag=main(dp[i],dp[i-a])
                dp[i-a][n]-=1
                if flag:
                    tempdic=copy.copy(dp[i-a])
                    tempdic[n]+=1
                    dp[i]=tempdic
dic=dp[N]
a=""
dic=sorted([[str(i),dic[i]] for i in dic],key=lambda x:x[0],reverse=True)
for i,z in dic:
    for m in range(z):
        a+=i
print(a)
