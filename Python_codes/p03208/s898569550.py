N,K=map(int,input().split())

H=[]
for _ in range(N):
    H.append(int(input()))

M=10**10
H.sort()
for i in range(N-K+1):
    M=min(M,H[i+K-1]-H[i])
print(M)
