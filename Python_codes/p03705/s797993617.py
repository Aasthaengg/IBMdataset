N,A,B = map(int,input().split())

if B < A:
  ans = 0
elif N == 1:
  if A == B:
    ans = 1
  else:
    ans = 0
elif 1 < N:
  ans = (B-A) * (N-2) + 1

print(ans)
  
