N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = 0
for i,c in enumerate(t):
  if i == N-1:
    ans += T
  else:
    ans += min(T,t[i+1]-t[i])
print(ans)