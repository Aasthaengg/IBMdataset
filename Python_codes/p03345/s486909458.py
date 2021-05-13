A, B, C, K = map(int,input().split())
if K == 0 or K % 2 ==0:
  ans = A-B
else:
  ans = -(A-B)
if abs(ans) > 10**18:
  print("Unfair")
else:
  print(ans)