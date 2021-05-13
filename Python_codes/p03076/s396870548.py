# coding: utf-8
import itertools
import math
A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
List=[A,B,C,D,E]
ans=10000000
for i in itertools.permutations(List, 5):
    AList=list(i)
    R=0
    for i in range(5):
        if str(AList[i])[-1]!=0 and i!=4:
            R+=math.ceil((AList[i])/10)*10
        else:
            R+=AList[i]
    ans=min(ans,R)
    #print(AList)
    #print(ans)
print(ans)
