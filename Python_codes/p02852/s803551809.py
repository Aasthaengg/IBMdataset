n,m=map(int,input().split())
s=input()
s=s[::-1]
r,l,cnt,k,=0,0,0,0
ans=[]
while 1:
  while cnt<m:
    r+=1
    if r==n:
      ans.append(r-k)
      print(*ans[::-1])
      exit()
    if s[r]=='0':
      l=r
    cnt+=1
  if r-l==m:
    print(-1)
    exit()
  ans.append(l-k)
  k=l
  cnt=r-l