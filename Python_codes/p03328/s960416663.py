a,b=map(int, input().split())
d=b-a
t=0
while d>0:
  t+=d
  d-=1
print(t-b)