N,M = [int(i) for i in input().split()]

ans = [0]*M
for i in range(N):
    K,*A = [int(j) for j in input().split()]
    for k in range(K):
        ans[A[k]-1] += 1

print(ans.count(N))
