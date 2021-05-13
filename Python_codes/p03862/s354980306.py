N,x = map(int, input().split())
A = [int(i) for i in input().split()]

B = list(A)

ans1 = ans2 = 0
for i in range(N-1):
  if B[i]+B[i+1] > x:
    b = B[i]+B[i+1] - x
    ans1 += b
    B[i+1] -= b
    if B[i+1] < 0: B[i+1] = 0


B = list(A[::-1])
for i in range(N-1):
  if B[i]+B[i+1] > x:
    b = B[i]+B[i+1] - x
    ans2 += b
    B[i+1] -= b
    if B[i+1] < 0: B[i+1] = 0

print( min(ans1, ans2) )

