n,l=map(int,input().split())
dic={0:0}
for _ in range(n):
  w,v=map(int,input().split())
  tmp=sorted(list(dic.keys()),reverse=True)
  for key in tmp:
    if key+w not in dic:
      dic[key+w]=dic[key]+v
    else:
      dic[key+w]=max(dic[key]+v,dic[key+w])
tmp=sorted(list(dic.keys()))
ans=0
for key in tmp:
  if key>l:
    break
  ans=max(ans,dic[key])
print(ans)
