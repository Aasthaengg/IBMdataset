n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
e,m,d=0,0,0
for x in p:
    if x<=a:e+=1
    if a<x<=b:m+=1
    if b<x:d+=1
print(min(e,m,d))