n=int(input())
k=int(input())
ans=1
for i in range(n):
  ans=ans*2 if ans<=k else ans+k
print(ans)