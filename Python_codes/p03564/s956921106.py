N = int(input())
K = int(input())
 
ans = 1000000
 
for bi in range(1<<N):
  cnt = 1
  for i in range(N):
    if bi>>i&1:
      cnt *= 2
    else:
      cnt += K
  ans = min(ans, cnt)
print(ans)