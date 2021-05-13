MAX = 35
N = int(input())
ans = 1
for i in range(2,MAX+1):
  t = i*i
  while t <= N:
    ans = max(ans,t)
    t *= i
print(ans)
