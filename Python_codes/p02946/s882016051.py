N,K=map(int,input().split())

ans=[K]

for i in range(1,N):
    ans.append(K-i)
    ans.append(K+i)

ans.sort()


print(*ans)
