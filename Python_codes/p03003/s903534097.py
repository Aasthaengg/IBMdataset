D = 10**9+7
N, M = list(map(int,raw_input().split()))
S = list(map(int,raw_input().split()))
T = list(map(int,raw_input().split()))
a = [[0 for j in xrange(M+1)] for i in xrange(N+1)]
for i in xrange(N+1):
  a[i][0] = 1
for j in xrange(M+1):
  a[0][j] = 1
for i in xrange(N):
  for j in xrange(M):
    a[i+1][j+1] = (a[i][j+1]+a[i+1][j])%D
    if S[i]!=T[j]:
      a[i+1][j+1] = (a[i+1][j+1]-a[i][j])%D
print(a[N][M])