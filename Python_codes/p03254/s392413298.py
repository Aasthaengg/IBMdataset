n,x=map(int,input().split())
a=sorted(list(map(int,input().split())))

if sum(a)<x:
  cnt=n-1
else:
  ans=0
  cnt=0
  for i in range(n):
    ans+=a[i]
    cnt+=1
    if ans==x:
      break
    elif ans>x:
      cnt-=1
      break
print(cnt)