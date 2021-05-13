N,M,K=map(int,input().split())

ans="No"
for i in range(N+1):
    for j in range(M+1):
        cnt=i*j+(N-i)*(M-j)
        if cnt==K:
            ans="Yes"
            break

print(ans)