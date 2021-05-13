n=int(input())
s=[input() for _ in range(n)]
sdic={}
march=['M', 'A', 'R', 'C', 'H']
ans=0
for i in range(n):
  if s[i][0] in march:
    if s[i][0] in sdic:
      sdic[s[i][0]]+=1
    else:
      sdic[s[i][0]]=1
lis=[_ for _ in sdic.values()]
for j in range(len(lis)-2):
  for k in range(j+1,len(lis)-1):
    for l in range(k+1,len(lis)):
      ans+=lis[j]*lis[k]*lis[l]
print(ans)