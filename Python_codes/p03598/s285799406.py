n = int(input())
k = int(input())
xl = list(map(int, input().split()))

ans = 0
for i in range(n):
  if xl[i] <= k // 2:
    ans += xl[i]*2
  else:
    ans += (k - xl[i])*2

print(ans)
    

