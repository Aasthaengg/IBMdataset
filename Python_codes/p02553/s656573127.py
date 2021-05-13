a,b,c,d = map(int, input().split())
ans = -(10**20)
for i in (a,b):
  for j in (c,d):
    ans = max(ans,i*j)
print(ans)
