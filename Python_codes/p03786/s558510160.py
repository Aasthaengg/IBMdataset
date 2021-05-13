n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=1
s=sum(a)-a[-1]
for i in range(n-1):
  if 2*s>=a[n-i-1]:
    ans+=1
    s-=a[n-i-2]
  else:
    break
print(ans)