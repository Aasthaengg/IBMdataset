N=int(input())
a=list(map(int,input().split()))
ans = 0
res =1
for i in range(N):
  if res  != a[i]:
    ans += 1
  elif  res == a[i]:
        res += 1
if ans ==N:
  print(-1)
else:
  print(ans)