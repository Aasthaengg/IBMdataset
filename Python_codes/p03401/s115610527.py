# coding: utf-8
N=int(input())
A=list((map(int,input().split())))
A.insert(0,0)

d=[]
skip_d=[]

for i in range(N):
    d.append(abs(A[i+1]-A[i]))
    if i<N-1:
        skip_d.append(abs(A[i+2]-A[i]))
    else:
        skip_d.append(abs(A[0]-A[i]))

d.append(abs(A[-1]))

sum_d=sum(d)

for i in range(N):
    ans=sum_d-(d[i]+d[i+1])+skip_d[i]
    
    print(ans)