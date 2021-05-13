n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
ssum=sum(a)
ans=1
for i in range(n):
  ssum-=a[i]
  if 2*ssum<a[i]:
    break
  else:
    ans+=1
print(ans)