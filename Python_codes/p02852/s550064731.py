n,m=map(int,input().split())
s=[int(s) for s in input()][::-1]
i=0
k=m
cnt=0
a=[]
while i<n:
  j=-1
  while i<n and k:
    k-=1
    i+=1
    if s[i]==0:j=i
  if j==-1:
    print(-1)
    exit()
  a+=[j]
  k=m-i+j
  cnt+=1
for i in range(len(a)-1,0,-1):
  a[i]-=a[i-1]
print(*a[::-1])