#python 2.7
n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab=sorted(ab,key=lambda x:x[0])
res=ans=0
for i in range(n):
  if res+ab[i][1]>=m:
    ans+=(ab[i][0])*(m-res)
    break
  else:
    ans+=(ab[i][0])*ab[i][1]
    res+=ab[i][1]
print(ans)