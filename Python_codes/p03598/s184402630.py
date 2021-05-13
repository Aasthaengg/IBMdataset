N = int(input())
K = int(input())
X = list(map(int,input().split()))
ans = 0

for n in range(N):
  ans+=min(X[n]*2,(K-X[n])*2)
print(ans)