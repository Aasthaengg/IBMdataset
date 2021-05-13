N,M,K=map(int,input().split())

ans='No'
i=0
while i<=N:
    j=0
    while j<=M:
        if M*i+N*j-2*i*j==K:
            ans='Yes'
        j+=1
    i+=1

print(ans)