n=int(input())
xl=[list(map(int,input().split())) for _ in range(n)]
lr=[[xl[i][0]-xl[i][1],xl[i][0]+xl[i][1]] for i in range(n)]
lr.sort(key=lambda x:x[1])
ans=n
r=lr[0][1]
for i in range(1,n):
  if lr[i][0]<r:
    ans-=1
  else:
    r=lr[i][1]
print(ans)