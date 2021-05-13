h,n=map(int,input().split())
a=[int(x) for x in input().rstrip().split()]

if h<=sum(a):
  print("Yes")
else:
  print("No")
