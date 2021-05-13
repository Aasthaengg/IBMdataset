import bisect

N, H=map(int, input().split())
a=[0]*N
b=[0]*N
for i in range(N):
  a[i], b[i]=map(int, input().split())
  
a=max(a)
b.sort()
tmp=bisect.bisect_right(b, a)
if tmp==N:
  print((H-1)//a+1)
  exit()

b=b[tmp:]
b=b[::-1]
ans=0
for i in range(len(b)):
  H-=b[i]
  ans+=1
  if H<=0:
    print(ans)
    exit()
ans+=(H-1)//a+1
print(ans)