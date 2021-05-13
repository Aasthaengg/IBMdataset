A = list(map(int,input().split()))
if A[1] + A[2] < A[0]:
  b = 0
else:
  b = A[1] + A[2] - A[0]
x = [A[1], A[2]]
print(min(x) ,b)