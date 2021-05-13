n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
ab.reverse()
ans=0
for i in range(n):
  d=ab[i][0]+ans
  if d%ab[i][1]!=0:
    ans+=ab[i][1]-d%ab[i][1]
print(ans)