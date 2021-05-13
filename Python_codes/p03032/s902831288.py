N,K=map(int,input().split())
vlist=list(map(int,input().split()))

#take i and remove K-i
answer=0
for i in range(K+1):
  if i>N: break
  
  take_cand=[]
  if i==N:
    take_cand=[vlist]
  else:
    for j1 in range(i+1):
      j2=i-j1
      take_cand.append(vlist[:j1]+vlist[N-j2:])
  
  #print(i,take_cand)
  for take in take_cand:
    take.sort(reverse=True)
    for _ in range(K-i):
      if len(take)>0 and take[-1]<0:
        take.pop()
    
    answer=max(sum(take),answer)

print(answer)