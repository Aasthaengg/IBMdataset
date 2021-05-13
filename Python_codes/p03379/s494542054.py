N = int(input())
X = list(map(int, input().split()))
XI = [[X[i], i] for i in range(N)]
XI.sort()
A = [0]*N
for k in range(N):
  x, i = XI[k]
  if k < N//2:
    A[i] = XI[N//2][0]
  else:
    A[i] = XI[N//2 - 1][0]
for a in A:
  print(a)