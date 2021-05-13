n=int(input())
dict={}
ans=0
for i in range(n):
  s=str(sorted(input()))
  if s in dict:
    dict[s]+=1
    ans+=(dict[s]-1)
  else:
    dict[s]=1
print(ans)