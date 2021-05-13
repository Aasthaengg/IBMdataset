N=int(input())
a=list(map(int,input().split()))
a.sort()
a.append(0)
ans=0
b=a[0]
c=0
for i in range(N+1):
  if b!=a[i]:
    if c<b:
      ans+=c
    b=a[i]
    c=1
  else:
    if c==b:
      ans+=1
    else:
      c+=1
print(ans)