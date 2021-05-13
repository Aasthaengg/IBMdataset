s=1
ans=0
a,b=map(int,input().split())
while b>s:
  s+=a-1
  ans+=1

print(ans)