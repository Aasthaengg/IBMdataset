# coding: utf-8
n=int(input())
a=[]
a=list(map(int,input().split()))
count=0
for i in reversed(a):
    print (i,end="")
    count+=1
    if count!=n:
        print(" ",end="")
    else :
        print("")

