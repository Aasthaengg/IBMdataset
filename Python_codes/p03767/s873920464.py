N=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
ans=0
for i in range(2*N):
  if i%2==1:
    ans+=a[i]
print(ans)
