m,k = map(int, input().split())
if 2**m <= k:
  print(-1) 
elif (m,k) == (1,0):
  print("0 0 1 1")
elif (m,k) == (1,1):
  print(-1)
else:
  l = [x for x in range(2**m) if x != k]
  ans = l+[k]+l[::-1]+[k]
  print(" ".join(map(str,ans)))