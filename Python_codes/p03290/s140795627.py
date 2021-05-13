d,g=map(int,input().split())
pc=[list(map(int,input().split())) for i in range(d)]
ans=10**18
for i in range(2**d):
  t_point,t_solved=0,0
  for j in range(d):
    if i&(1<<j):
      t_solved+=pc[j][0]
      t_point+=pc[j][0]*(j+1)*100+pc[j][1]
  if t_point>=g:
    ans=min(ans,t_solved)
    continue
  
  j=d-1
  while j>=0:
    if i&(1<<j):
      j-=1
      continue
    p,c=pc[j]
    point=(j+1)*100
    if t_point+(p-1)*point<g:
      t_point+=(p-1)*point
      t_solved+=p-1
    else:
      husoku=g-t_point
      count=-(-husoku//point)
      t_point+=count*point
      t_solved+=count
    if t_point>=g:
      break
    j-=1
  else:
    continue
  if t_point>=g:
    ans=min(ans,t_solved)
print(ans)



