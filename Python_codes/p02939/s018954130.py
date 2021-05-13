s=input()
a=len(s)
cnt=0
l=0
r=1
W='aaa'
while r<a+1:
  if s[l:r]!=W:
    cnt+=1
    W=s[r-1:r]
    r+=1
    l=r-1
  else:
    cnt+=1
    W=s[r-1:r+1]
    r+=2
    l=r-1
if r!=a+1:
  cnt-=1
print(cnt)