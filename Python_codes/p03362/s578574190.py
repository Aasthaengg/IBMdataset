P=[1 for i in range(55556)]
P[0]=0
P[1]=0
for i in range(2,55556):
    if P[i]==1:
        for j in range(2,55556):
            if i*j<=55555:
                P[i*j]=0
            else:
                break

ans=[]
for i in range(55556):
    if P[i]==1 and i%10==1:
        ans.append(i)
N=int(input())
print(*ans[:N])