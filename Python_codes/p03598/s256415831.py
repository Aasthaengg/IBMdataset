n = int(input())
k = int(input())
X = list(map(int, input().split()))

ans = 0
for i in range(n):
  if X[i] <= k/2:
    ans += 2*abs(X[i])
  else:
    ans += 2*abs(X[i] - k)
 
print(ans)