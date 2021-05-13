N,K=map(int,input().split())
res = K
for _ in range(N-1):
    res*=(K-1)
print(res)