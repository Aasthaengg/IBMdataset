d,g=map(int,input().split())
pc_=[list(map(int,input().split())) for _ in range(d)]
pc=[[(i+1)*100,pc[0],pc[1]] for i,pc in enumerate(pc_)]
n=d
ans=1000
for i in range(2**n):
  all_ac=[]
  no_ac=[]
  for j in range(n):
    if ((i>>j) & 1):#立っているビットのところで処理が走る
      all_ac.append(j)
    else:
      no_ac.append(j)
  score=sum([pc[j][2]+pc[j][0]*pc[j][1] for j in all_ac])
  n_ac=sum([pc[j][1] for j in all_ac])
  tmp=g-score
  while no_ac and tmp>0:
    a=no_ac.pop()
    i,p,c=pc[a]
    if tmp<=i*(p-1):
      n_ac+=(tmp+i-1)//i
      tmp=0
    else:
      n_ac+=p-1
      tmp-=i*(p-1)
  if tmp<=0:
    ans=min(n_ac,ans)
print(ans)