s=input()
l=len(s)
ans=1+(l*(l-1))//2
dic={}
for t in s:
  if t not in dic:
    dic[t]=1
  else:
    dic[t]+=1
for val in dic.values():
  ans-=(val*(val-1))//2
print(ans)