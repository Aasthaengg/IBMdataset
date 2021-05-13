n,m = map(int,input().split())
cnt = 0
for i in range(n+1):
  for j in range(n+1):
    if m-i-j <= n and m-i-j >= 0:
      cnt += 1	
print(cnt)