N,M = map(int,input().split())

if N == 1 and M == 1:
  ans = 1
elif N == 1 or M == 1:
  ans = N * M - 2
elif N == 2 or M == 2:
  ans = 0
else:
  ans = (N - 2) * (M - 2)
  
print(ans)