N = int(input())
A = [int(input()) for n in range(N)]
B = sorted(A)[::-1]
a1 = B[0]
a2 = B[1]

if a1==a2:
  for n in range(N):
    print(a1)
else:
  for n in range(N):
    if A[n]==a1:
      print(a2)
    else:
      print(a1)