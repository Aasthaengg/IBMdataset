N=int(input())
ans=[0 for a in range(11000)]
for i in range(1,101):
  for x in range(1,101):
    for y in range(1,101):
      v=x*x+y*y+i*i+x*y+y*i+i*x
      if v<=N:
        ans[v]+=1
for b in range(1,N+1):
  print(ans[b])