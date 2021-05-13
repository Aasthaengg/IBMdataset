s=input()
n=len(s)
k=0
l=1
r=2
j=s[0]
cnt=1
ans=[]
while r<=n:
  if s[l:r]==j:
    r+=1
  else:
    j=s[l:r]
    ans+=[j]
    l=r
    r+=1
    cnt+=1
print(cnt)