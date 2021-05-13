n = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(2, n):
  if P[i-2] < P[i-1] < P[i] or P[i-2] > P[i-1] > P[i]:
  	ans += 1
print(ans)