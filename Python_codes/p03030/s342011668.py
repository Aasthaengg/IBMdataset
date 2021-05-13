N = int(input())
A = []
for i in range(N):
  a = list(input().split())
  A.append([a[0], -int(a[1]), i+1])
A.sort()
for i in range(N):
  print(A[i][2])