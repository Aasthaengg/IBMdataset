A,B,X = map(int,input().split())
if A == X:
  print("YES")
elif X > A and X <= A+B:
  print("YES")
else:
  print("NO")
