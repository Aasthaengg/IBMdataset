N = int(input())
A = input()
B = input()
C = input()

res = 0
for i in range(N):
  ab = (A[i] == B[i])
  bc = (B[i] == C[i])
  ca = (C[i] == A[i])
  s = ab*1 + bc*1 + ca*1

  if (0 == s):
    res += 2
  elif (1 == s):
    res += 1
print(res)
