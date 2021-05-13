n=int(input())
a=list(map(int,input().split()))
ch=[0]*(n+1)
kai=[0]
for i in a:
  ch[i]+=1
for i in range(n):
  kai.append(kai[i]+i+1)
ans=0
for i in ch:
  if i==0:
    continue
  ans+=kai[i-1]
for i in a:
  print(ans-(kai[ch[i]]-kai[ch[i]-1])+1)