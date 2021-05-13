import collections

ans=0
dic={}
n=int(input())
for i in range(n):
  s=input()
  sl=[i for i in s]
  sl.sort()
  ss=tuple(sl)

  if ss not in dic:
    dic[ss]=1
  else:
    ans+=dic[ss]
    dic[ss]+=1

print(ans)