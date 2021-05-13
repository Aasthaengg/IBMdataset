N=int(input())
res=[]
for i in range(N):
  a,b=map(int,input().split())
  res.append((a+b,a,b))
  
res = sorted(res,reverse=True)

ans=0
for i in range(N):
  if i % 2== 0:
    ans += res[i][1]
  else:
    ans -= res[i][2]
    
print(ans)