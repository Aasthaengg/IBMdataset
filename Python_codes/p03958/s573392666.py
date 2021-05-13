K,T = map(int,input().split())
A = list(map(int,input().split()))
minA = min(A)
maxA = max(A)
sumA = sum(A)

if len(A) == 1:
  ans = A[0]-1
else:
  ans = max(0,maxA-1-(sumA-maxA))

print(ans)
