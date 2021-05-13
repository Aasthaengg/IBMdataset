N = int(input())
A = [int(input()) for _ in range(N)]
A_sort = sorted(A)
M_1, M_2 = A_sort[-1], A_sort[-2]
for a in A:
  if a == M_1:
    print(M_2)
  else:
    print(M_1)