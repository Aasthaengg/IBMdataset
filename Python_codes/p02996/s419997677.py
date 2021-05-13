n=int(input())
d=[]
for _ in range(n):
  a,b=map(int,input().split())
  d+=[(b,a)]
d=sorted(d)
t=0
for i,j in d:
  if j+t>i:
    print('No')
    break
  t+=j
else:print('Yes')