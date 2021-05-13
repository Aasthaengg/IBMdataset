N, T = map(int, input().split())
t = list(map(int, input().split()))
t.append(t[-1])
ans = 0
for i in range(1, N+1):
  if t[i] - t[i-1] > T:
    ans += T
  elif t[i] == t[i-1]:
    ans += T
  elif t[i] - t[i-1] <= T:
    ans += t[i] - t[i-1]
  
print(ans)