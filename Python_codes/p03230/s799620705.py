n,k=int(input()),0
for i in range(int((2*n)**0.5)+10):
    if i*(i-1)==2*n:
        k=i
if k==0:
    print('No')
else:
    print('Yes')
    print(k)
    c=1
    a=[[0]*k for _ in range(k)]
    for i in range(1,k):
        for j in range(1,i+1):
            a[i][j]=c
            c+=1
    ans=[[k-1]+[a[i][i] for i in range(1,k)]]
    for i in range(1,k):
        l=[k-1]
        h,w=i,1
        for j in range(1,k):
            l.append(a[h][w])
            h,w=(h,w+1) if j<i else (h+1,w)
        ans.append(l)
    for i in ans:
        print(*i)