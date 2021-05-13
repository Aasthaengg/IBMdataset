N = int(input())
A = [int(input()) for _ in range(N)]

max_1 = sorted(A)[N-1]
max_2 = sorted(A)[N-2]
for i in range(N):
  if A[i] == max_1:
    print(max_2)
  else:
    print(max_1)
