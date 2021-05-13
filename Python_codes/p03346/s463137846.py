n = int(input())
a = [int(input()) for i in range(n)]
ls = [0 for i in range(n)]
for i in range(n):
  x = a[i]
  ls[x-1] = i+1
cnt = 1
ans = 0
ls.append(0)
for i in range(1,n+1):
  if ls[i]>ls[i-1]:
    cnt += 1
  else:
    ans = max(ans,cnt)
    cnt = 1
print(n-ans)