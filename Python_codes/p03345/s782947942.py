A,B,C,K = map(int,input().split())
if(K == 0):
  ans = A - B
elif(K % 2 == 1):
  ans = B - A
else:
  ans = A - B
if(ans > 10 ** 18):
  print("Unfair")
else:
  print(str(ans))