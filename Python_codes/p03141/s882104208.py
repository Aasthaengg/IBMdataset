# coding: utf-8
N=int(input())
AB=[]

for i in range(N):
    A,B=map(int,input().split())
    AB.append([A+B,A,B])

AB.sort(reverse=True)
Ta=0
Ao=0

for i in range(N):
    if i%2==0:
        Ta+=AB[i][1]
    else:
        Ao+=AB[i][2]

print(Ta-Ao)


