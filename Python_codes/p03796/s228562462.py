a=int(input())
ans=1
for i in range(a):
  ans=ans*a%(10**9+7)
  a=a-1
print(ans)