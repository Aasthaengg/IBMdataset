N=int(input())
B=[]
for i in range (N):
    a=int(input())
    b=[]
    for j in range(a):
        x,y=map(int,input().split())
        b.append([x,y])
    B.append(b)
ans=0
for k in range(2**N):
    num=0
    L=[0]*N
    p=0
    for j in range(N):
        if ((k>>j)&1):
            L[N-1-j]=1
            num+=1
    for k in range(N):
        if L[k]==1:
            for m in range(len(B[k])):
                if L[B[k][m][0]-1]!=B[k][m][1]:
                    p=1
    if p==0:
        ans=max(ans,num)

print(ans)