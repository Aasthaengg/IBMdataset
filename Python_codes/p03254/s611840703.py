n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort(key=int)
ans=0
for i in range(n):
  x=x-a[i]
  if x<0:
    x=x+a[i]
  else:
    ans+=1
if ans==n:
    if x>0:
        print(ans-1)
    else:
        print(ans)
else:
    print(ans)