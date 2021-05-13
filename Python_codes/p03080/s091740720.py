N = int(input())
S = input()
A = [0, 0]
for i in range(N):
  if S[i] == 'R':
    A[0] += 1
  else:
    A[1] += 1
if A[0] > A[1]:
  print("Yes")
else:
  print("No")