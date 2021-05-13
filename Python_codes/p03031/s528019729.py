n,m=map(int,input().split())
k=[0]*m
s=[[0 for j in range(n)] for i in range(m)]
for i in range(m):
  x = list(map(int,input().split()))
  k = x[0]
  for j in range(1, k+1):
    s[i][x[j]-1] = 1
p=list(map(int,input().split()))

ans = 0
for x in range(2**n):
  for i in range(m):
    cnt = 0
    for j in range(n):
      if (x >> j & 1) and s[i][j]:
        cnt += 1
    if cnt % 2 != p[i]:
      break
  else:  # breakしなかった=すべて一致した場合のみ
    ans += 1
print(ans)