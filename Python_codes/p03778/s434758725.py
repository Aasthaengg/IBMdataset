w,a,b=map(int, input().split())

A=min(a,b)

B=max(a,b)

if A+w<B:
  print(B-A-w)
else:
  print(0)