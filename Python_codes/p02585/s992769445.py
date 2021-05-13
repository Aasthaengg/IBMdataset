n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))

ans=-float('inf')
for i in range(n):
  T=1
  index=p[i]-1
  T_score=c[index]
  flag=True
  while flag:
    T+=1
    index=p[index]-1
    T_score+=c[index]
    if index==i:
      flag=False
  #場合分け開始
  if T>=k:
    score_list=[c[p[i]-1]]+[0]*(k-1)
    index=p[i]-1
    for s in range(1,k):
      index=p[index]-1
      score_list[s]=score_list[s-1]+c[index]
    score=max(score_list)
  else:
    if T_score<=0:
      score_list=[c[p[i]-1]]+[0]*(T-1)
      index=p[i]-1
      for s in range(1,T):       
        index=p[index]-1
        score_list[s]=score_list[s-1]+c[index]        
      score=max(score_list)
    else:
      m1=k//T
      m2=k%T
      score_list=[c[p[i]-1]]+[0]*(T+m2-1)
      index=p[i]-1
      for s in range(1,T+m2):
        index=p[index]-1
        score_list[s]=score_list[s-1]+c[index]
      score=max(score_list)+T_score*(m1-1)
  ans=max(ans,score)
print(ans)