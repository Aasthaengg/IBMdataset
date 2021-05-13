N,K=map(int,input().split())
P=10**9+7

L=[0]*(K+1)
for i in range(1,K+1)[::-1]:
    minus=0
    count=2
    while True:
        if count*i<=K:
            minus+=L[count*i]
            minus=minus%P
            count+=1
        else:
            break

    L[i]=(pow(K//i,N,P)-minus)%P

ans=0
for j in range(1,K+1):
    ans+=j*L[j]
    ans=ans%P

print(ans)