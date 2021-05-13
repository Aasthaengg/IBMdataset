n = int(input())
A = [0] + list(map(int, input().split())) + [0]
C = []
c = 0
for i in range(n+1):
  c += abs(A[i+1] - A[i])
for i in range(1, n+1):
  if A[i-1] <= A[i] <= A[i+1] or A[i+1] <= A[i] <= A[i-1]:
    print(c)
  elif A[i] <=A[i-1] <= A[i+1] or A[i] <= A[i+1] <= A[i-1]:
    print(c - abs(min(A[i-1], A[i+1]) - A[i])*2)
  else:
    print(c - abs(A[i] - max(A[i+1], A[i-1]))*2)