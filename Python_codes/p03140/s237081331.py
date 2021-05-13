N = int(raw_input())
A = list(raw_input())
B = raw_input()
C = raw_input()
con = 0
for i in range(N):
  if A[i] != B[i] and B[i] != C[i] and A[i] != C[i]:
    con += 2
  elif A[i] != B[i]:
    con += 1
  elif B[i] != C[i]:
    con += 1
  elif A[i] != C[i]:
    con += 1

print con