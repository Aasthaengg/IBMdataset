n = int(input())
d = list(map(int,input().split()))
ans = 0
for i in range(n):
  for j in range(n):
    ans += d[i]*d[j]
for k in range(n):
  ans -= d[k]**2
print(ans//2)