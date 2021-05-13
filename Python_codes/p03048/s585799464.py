R,G,B,N=map(int,input().split())

cnt=0
for r in range(N+1):
  for g in range(N+1):
    u=N-R*r-G*g
    if u<0:
      break
    if u%B!=0:
      continue
    if u//B>=0:
      cnt+=1
print(cnt)
