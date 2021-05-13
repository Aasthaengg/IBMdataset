A,B,C=map(int,input().split())
ans=int(0)
pay=int(0)
for i in range(1,C+1):
  pay+=A
  if pay<=B:
    ans+=1
  else:
    break
print(ans)