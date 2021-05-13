A,B,C,K = map(int,input().split())

limit = 10 ** 18

if K % 2 == 0:
  ans = (A - B)
else:
  ans = (B - A)
  
if ans < limit:
  print(ans)
else:
  print("Unfair")