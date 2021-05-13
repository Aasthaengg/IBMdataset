n=int(input())
a=list(map(int,input().split()))
a.sort()

m=0
ma=0
for i in a:
  t=min(i,a[-1]-i)
  if m<t:
    m=t
    ma=i
print(a[-1],ma)