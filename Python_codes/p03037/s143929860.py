n,m=map(int,input().split())
max_ = 0
min_ = n+1
for i in range(m):
  a,b=map(int, input().split())
  max_ = max(max_, a)
  min_ = min(min_, b)
#print(max_, min_)
if(min_ < max_):print(0)
else:print(min_-max_+1)