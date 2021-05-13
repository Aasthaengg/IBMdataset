N,K,S = map(int,input().split())

ans = []

for i in range(N):
    if i < K:
        ans.append(S)
    elif S == 10**9:
        ans.append(S-1)
    else:
        ans.append(S+1)
print(*ans)