A, B, X = list(map(int, input().split()))

if X < A or A + B < X: 
  print("NO")
else:
  print("YES")