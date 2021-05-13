n,m=map(int,input().split())
mise=[]
for i in range(n):
  mise.append(list(map(int,input().split())))
ans=0
mise.sort()
i=0
while m>mise[i][1]:
  ans+=mise[i][0]*mise[i][1]
  m-=mise[i][1]
  i+=1
ans+=m*mise[i][0]
print(ans)