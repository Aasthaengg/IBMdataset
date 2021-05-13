n=int(input())
pw=1
for i in range(n):
  pw=pw*(i+1)%(10**9+7)
ans=pw
print(ans)