n,m,x=map(int,input().split())
A=list(map(int,input().split()))
a1=0
a2=0
for a in A:
    if a<x:
        a1+=1
    else:
        a2+=1
print(min(a1,a2))