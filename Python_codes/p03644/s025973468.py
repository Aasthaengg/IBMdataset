ma=-1
for i in range(1,int(input())+1):
  cnt=0
  x=i
  while x&1==0:
    x//=2
    cnt+=1
  if ma<cnt:
    ma=cnt
    ans=i
print(ans)