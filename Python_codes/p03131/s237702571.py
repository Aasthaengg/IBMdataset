K, A, B = map(int, input().split())
if A+1>= B:
  ans = K+1
else:
  if K-A-1 < 0:
    n = 0
    ans = K+1
  else:
    n = (K-A-1)//2
    m = (K-A-1)%2
    ans = n*(B-A) + m + B
print(ans)