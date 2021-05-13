N,M,Q = map(int,input().split())
S = [[0]*(N+1) for _ in range(N+1)]
ans = [0]*Q

for i in range(M):
    l,r = map(int,input().split())
    S[l][r] += 1

for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j] += S[i-1][j]+S[i][j-1]-S[i-1][j-1]

for i in range(Q):
    p,q = map(int,input().split())
    ans[i] = S[q][q] - S[p-1][q] - S[q][p-1] + S[p-1][p-1]

print("\n".join(map(str,ans)))