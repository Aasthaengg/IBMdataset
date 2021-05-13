N, A, B, C, D = map(int, input().split())
S = '.'+input()

def dp(s,g):
  if s==g or s==g-1 or s==g-2:
    return 1
  if S[s+1]=='.' and S[s+2]=='.':
    return DP[s+1]|DP[s+2]
  if S[s+1]=='#' and S[s+2]=='.':
    return DP[s+2]
  if S[s+1]=='.' and S[s+2]=='#':
    return DP[s+1]
  if S[s+1]=='#' and S[s+2]=='#':
    return 0
DP=[0]*(N+1)
for i in range(C,A-1,-1):
  DP[i] = dp(i,C)
ansA = DP[A]
for i in range(D,B-1,-1):
  DP[i] = dp(i,D)
ansB = DP[B]
#print(ansA,ansB)
if C<D:
  ans = ansA & ansB
else:
  ans = ansA & ansB & ('...' in S[B-1:D+2])

Ans = ['No','Yes']
print(Ans[ans])