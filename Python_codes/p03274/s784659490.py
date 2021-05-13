from bisect import bisect_left, bisect_right

N,K  = map(int, input().split())

X = list(map(int, input().split()))
Ne = bisect_left(X, 0)
Po = bisect_right(X, 0)

if Ne != Po:
  K -= 1

ans = 10**9

for i in range(K+1):
  tmp = 10**9
  if i > N - Po:
    continue
  if K - i > Ne:
    continue
  
  if i == 0:
    tmp = abs(X[Ne-K])
  
  elif i == K:
    tmp = abs(X[Po+K-1])
  
  else:
    tmp = X[Po+i-1] - X[Ne-(K-i)] + min(abs(X[Po+i-1]),abs(X[Ne-(K-i)])) 

  ans = min(ans,tmp)

print(ans) 