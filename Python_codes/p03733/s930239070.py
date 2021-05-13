N, T = map(int, input().split())
t = list(map(int, input().split()))
X = T
for i in range(1, N):
  if t[i]-t[i-1]<=T: X += (t[i]-t[i-1])
  else: X += T
print(X)