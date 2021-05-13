# coding: utf-8
# Your code here!
import sys
import itertools
import math

n=int(input())
point=[]

for i in range(n):
    arr=list(map(int,input().split()))
    point.append(arr)
ans=[]
l = [i for i in range(n)]

for v in itertools.permutations(l, n):
    dist=0
    for j in range(len(v)-1):
        dist+=math.sqrt(math.pow((point[v[j]][0]-point[v[j+1]][0]),2)+math.pow((point[v[j]][1]-point[v[j+1]][1]),2))
    ans.append(dist)
print(sum(ans)/len(ans))