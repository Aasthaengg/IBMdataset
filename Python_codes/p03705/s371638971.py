N, A, B = map(int, input().split())

if N==1 and A==B:
  ans = 1
elif N==1:
  ans = 0
elif A > B:
  ans = 0
else:
  ans = (B-A) * (N-2) + 1
print(ans)