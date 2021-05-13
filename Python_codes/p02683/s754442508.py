N,M,X=map(int,input().split())

A=[0]*N
for j in range(N):
    A[j]=[int(x) for x in input().split()]
money=10**7
for i in range(2**N):
    read=[0]*N #その本を読むか否か
    for h in range(N):
        if i%2==1:
            read[h]=1
        i//=2
    understanding=[0]*M
    kouho=0
    for k in range(N):
        if read[k]==1:
            kouho+=A[k][0]
            for m in range(1,M+1):
                understanding[m-1]+=A[k][m]
    if min(understanding)>=X:
        money=min(money,kouho)
if money==10**7:
    print(-1)
else:
    print(money)
