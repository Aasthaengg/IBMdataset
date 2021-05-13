N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A)
bool = 1 if B[-1] == B[-2] else 0
for i in range(N):
  if bool:
    print(B[-1])
  else:
    if A[i] == B[-1]:
      print(B[-2])
    else:
      print(B[-1])