N = int(input())
A = list(map(int, input().split()))
l = 0
r = N - 1
L = A[l]
R = A[r]
while r-l!=1:
  if L>=R:
    R += A[r-1]
    r -= 1
  else:
    L += A[l+1]
    l += 1
print(abs(L-R))
