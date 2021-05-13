A, B, X = map(int, input().split())

if X <= A + B - 1 and X >= A:
  print("YES")
else:
  print("NO")