n=int(input())
dic={}
for i in range(n):
  tmp="".join(sorted(list(input().strip())))
  dic[tmp]=dic.get(tmp,0)+1
ans=0
for k in dic.keys():
  if dic[k] >= 2:
    ans+=(dic[k]*(dic[k]-1))//2
print(ans)