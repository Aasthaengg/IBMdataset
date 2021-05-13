h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
ans=[0 for _ in range(h*w)]
i=0
c=1
for x in a:
  while x>0:
    ans[i]=c
    x-=1
    i+=1
  c+=1

for i in range(h):
  grd=ans[w*i:w*(i+1)]
  if i%2==1:
    grd=grd[::-1]
  print(*grd)


#print(ans)