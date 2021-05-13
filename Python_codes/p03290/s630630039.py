d,g=map(int,input().split())
pc=[list(map(int,input().split())) for _ in range(d)]
ans=float('inf')
for i in range(2**d):
  al=[]
  notal=[]
  anstmp=0
  score=0
  for j in range(d):
    if (i>>j)&1:al.append(j)
    else:notal.append(j)
  for j in al:
    score+=(j+1)*100*pc[j][0]
    score+=pc[j][1]
    anstmp+=pc[j][0]
  while notal and score<g:
    j=notal.pop()
    k=(g-score+(j+1)*100-1)//((j+1)*100)
    k=min(k,pc[j][0]-1)
    score+=(j+1)*100*k
    anstmp+=k
  if score>=g:ans=min(ans,anstmp)
print(ans)

