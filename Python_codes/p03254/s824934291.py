N,x=map(int,input().split())
a=[int(x) for x in input().split()]
a.sort()
count=0
if sum(a)==x:
  count=N
elif sum(a)<x:
  count=N-1
else:
  for i in range(N):
    if sum(a[:i])<=x and sum(a[:i+1])>x:
      count=i
print(count)