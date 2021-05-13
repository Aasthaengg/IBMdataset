N = int(input())
ans = 1
inf = 10**9+7
for i in range(N):
  ans = (ans*(i+1))%inf
print(ans)