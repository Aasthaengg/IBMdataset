n,a,b=map(int,input().split())
cnt=0
for i in range(1,n+1):
  isum=0
  ii=i
  while ii>0:
    isum+=ii%10
    ii//=10
  if a<=isum<=b:
    cnt+=i
print(cnt)