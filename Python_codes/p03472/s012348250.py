# coding: utf-8
N,H=map(int,input().split())

A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

MA=max(A)
ans=0
B.sort()
k=-1

while B[k]>MA:
    H-=B[k]
    k-=1
    ans+=1
    if H<=0:
        break
    if k<-N:
        break
if H>=0:
    ans+=-(-H//MA)

print(ans)