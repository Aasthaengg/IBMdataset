n=int(input())
i=1
res=0
ans=[]
while res<n:
  res+=i
  ans.append(i)
  i+=1
if res-n!=0:
  ans.remove(res-n)
for p in ans:
  print(p)