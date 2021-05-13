D,G=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(D)][::-1]
ans=float("inf")
for i in range(2**D):
  S=0
  cnt=0
  q="{:0>10b}".format(i)[::-1]
  ads=q.find("0")
  for j in range(D):
    if int(q[j])&1:
      S+=(D-j)*100*li[j][0]+li[j][1]
      cnt+=li[j][0]
  if S<G and (D-ads)*100*(li[ads][0]-1)>=G-S:
    for k in range(li[ads][0]):
      S+=(D-ads)*100
      cnt+=1
      if S>=G:
        break
  if S>=G:
    ans=min(ans,cnt)
print(ans)