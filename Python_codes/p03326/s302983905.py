n,m=map(int,input().split())
xyz=[list(map(int,input().split()))for _ in range(n)]
def f(fx,fy,fz):
  t=[]
  for x,y,z in xyz:t.append(x*fx+y*fy+z*fz)
  t.sort(reverse=1)
  return sum(t[:m])
ans=0
ans=max(ans,f(1,1,1))
ans=max(ans,f(1,1,-1))
ans=max(ans,f(1,-1,1))
ans=max(ans,f(1,-1,-1))
ans=max(ans,f(-1,1,1))
ans=max(ans,f(-1,1,-1))
ans=max(ans,f(-1,-1,1))
ans=max(ans,f(-1,-1,-1))
print(ans)