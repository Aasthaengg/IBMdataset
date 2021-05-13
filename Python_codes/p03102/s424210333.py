N,M,C=map(int,input().split())
B = list(map(int, input().split()))
ans=0
for _ in range(N):
    A = list(map(int, input().split()))
    hantei=0
    for j in range(M):
        hantei+=A[j]*B[j]
    if hantei+C>0:
        ans+=1
print(ans)
