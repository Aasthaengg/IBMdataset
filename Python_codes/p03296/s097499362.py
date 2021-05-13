n=int(input())
a=list(map(int,input().split()))
ans=0
now=0
for i in range(n):
  if now != a[i]:
    now=a[i]
  else:
    now=0
    ans+=1
print(ans)