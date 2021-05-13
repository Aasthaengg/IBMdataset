N, K, S = map(int,input().split())


ans = []
for i in range(K):
    ans.append(S)
for j in range(N-K):
    if S != 10**9:
        ans.append(S+1)
    else:
        ans.append(100)
print(*ans)