N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A, reverse = True)
su = sum(A)
check = True
for i in range(M):
  if A[i] < su * 1/(4*M):
    check = False
if check:
  print("Yes")
else:
  print("No")