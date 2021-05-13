N=int(input())
F1=[]
F2=[]
for i in range(N):
    F=list(map(int,input().split()))
    F1.append(F[::2])
    F2.append(F[1::2])
P=[list(map(int,input().split())) for _ in range(N)]

ans=-float("inf")
for i in range(1,2**10):
    F_am=[0]*5
    F_pm=[0]*5
    for j in range(5):
        F_am[j]=i%2
        i//=2
        F_pm[j]=i%2
        i//=2
    c=[0]*N
    for j in range(N):
        for k in range(5):
            if F_am[k]==1 and F1[j][k]==1:
                c[j]+=1
            if F_pm[k]==1 and F2[j][k]==1:
                c[j]+=1
    val=0
    for j in range(N):
        val+=P[j][c[j]]
    ans=max(ans,val)
print(ans)