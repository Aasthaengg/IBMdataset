# coding: utf-8
S=list(input())
K=int(input())
N=len(S)

L=[]

for i in range(N):
    L.append((26-(ord(S[i])-ord("a")))%26)

for i in range(N):
    if K>=L[i]:
        S[i]="a"
        K-=L[i]

if K>0:
    S[-1]=chr(ord("a")+((ord(S[-1])+K-ord("a"))%26))

print("".join(S))