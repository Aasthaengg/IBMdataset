N, K, S = map(int,input().split())
ans = []


for i in range(K):
    ans.append(S)
if S == 10**9:
    for j in range(N-K):
        ans.append(7)
else:
    for j in range(N-K):
        ans.append(S+1)
print(' '.join(map(str,ans)))
    

