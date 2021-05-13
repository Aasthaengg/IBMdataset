N,T = map(int,input().split())
t = list(map(int,input().split()))
ans=0
ter=-1
for x in t:
  if(x>=ter):
    ans+=T
  else:
    ans+=T-(ter-x)
  ter=x+T

print(ans)
