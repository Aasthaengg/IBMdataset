S=list(map(int,input().split()))
K=sorted(S)
ans=0
ans=K[-1]-K[-2]
rest=K[-1]-(ans+K[0])
if rest%2==0:
  ans+=rest//2
  print(ans)
else:
  ans+=(K[-1]+1-K[0]-ans)//2+1
  print(ans)