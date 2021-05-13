N,M=map(int,input().split())
AB=list()
for i in range(N):
  AB.append(list(map(int,input().split())))
AB.sort()
ans=0
for i in range(N):
  if M>=AB[i][1]:
    M-=AB[i][1]
    ans+=AB[i][0]*AB[i][1]
  else:
    ans+=M*AB[i][0]
    M=0
print(ans)