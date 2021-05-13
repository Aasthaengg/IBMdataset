N, M = map(int, input().split())

ans = 0

if N >= 3 and M >= 3:
  ans = (N - 2) * (M - 2) 
elif N == 2 or M == 2:
  ans = 0
elif N == 1 or M == 1:
  if N == 1 and M == 1:
    ans = 1
  else:
    ans = max(N, M) - 2
  
print(ans)