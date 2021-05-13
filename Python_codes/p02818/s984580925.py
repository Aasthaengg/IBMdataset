a, b, k = list(map(int,input().split()))
if a >= k:
  p = a - k
  print(str(p) + " " + str(b))
else:
  print("0 " + str(max(0, b - k + a)))