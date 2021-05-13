input()
K = int(input())
l = list(map(int,input().split()))
ans = 0
for i in range(len(l)):
  if (K - l[i]) <= (l[i] - 0):
    ans += (K - l[i]) * 2
  elif (l[i] - 0) < (K - l[i]):
    ans += (l[i] - 0) * 2
print(ans)