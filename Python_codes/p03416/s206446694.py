min_n, max_n = map(int,input().split())
ans = 0
for i in range(min_n, max_n+1):
  c = str(i)
  if c ==c[::-1]:
    ans+=1
print(ans)