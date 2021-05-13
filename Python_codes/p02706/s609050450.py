a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(b)>a[0]:
  print(-1)
elif sum(b)==a[0]:
  print(0)
else:
  print(a[0]-sum(b))
