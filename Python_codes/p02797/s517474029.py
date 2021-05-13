#56 C - Subarray Sum
N,K,S = map(int,input().split())


ans = []
if S == 10**9:
    for i in range(K):
        ans.append(S)
    for j in range(N-K):
        ans.append(1)
else:
    for i in range(K):
        ans.append(S)
    for j in range(N-K):
        ans.append(S+1)
print(*ans)