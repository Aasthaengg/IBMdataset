n,k=map(int,input().split())
s=input()
s01=[[1,s[0]]]
for i in range(1,n):
  if s[i]==s[i-1]:
    s01[-1][0]+=1
  else:
    s01.append([1,s[i]])
a=len([i0 for i0,i1 in s01 if i1=='0'])
if a<=k:
  print(n)
  exit()
# 累計和
si=0
sums=[0]
for s01i in s01:
  si+=s01i[0]
  sums.append(si)
ans=0
#print(s01)
#print(sums)
l=0 if s[0]=='0' else 1
for i in range(l,len(s01),2):
  l=max(0,i-1)
  r=min(len(sums)-1,2*k+i)
  #print(sums[r]-sums[l],i,l,r)
  ans=max(ans,sums[r]-sums[l])
print(ans)
