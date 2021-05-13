q=int(input())
lr=[list(map(int,input().split())) for _ in range(q)]
mr=0
for l,r in lr:
  mr=max(mr,r)
l=[1 for _ in range(mr+1)]
l[0],l[1]=0,0
s=[0 for _ in range(mr+1)]
for i in range(2,int(mr**(1/2))+1):
  x=i*2
  while x<=mr:
    l[x]=0
    x+=i
for i in range(2,mr+1):
  if l[i]==1 and l[(i+1)//2]==1:
    s[i]=s[i-1]+1
  else:
    s[i]=s[i-1]
for l,r in lr:
  print(s[r]-s[l-1])