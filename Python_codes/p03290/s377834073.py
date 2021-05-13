D,G = map(int,input().split())
P = [list(map(int,input().split())) for d in range(D)]
ans = 1000

for i in range(1<<D):
  s=0
  n=0
  for j in range(D):
    if i>>j&1==1:
      s+=100*(j+1)*P[j][0]+P[j][1]
      n+=P[j][0]
  for j in range(D-1,-1,-1):
    if i>>j&1==0:
      r = ((G-s)//100+j)//(j+1)
      if r>P[j][0]:
        n = 1000
      else:
        n+=max(r,0)
      break
  ans=min(ans,n)

print(ans)