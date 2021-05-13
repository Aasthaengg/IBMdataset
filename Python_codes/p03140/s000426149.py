N = int(input())
A = input()
B = input()
C = input()
ans = 0
for i in range(N):
  if A[i] != B[i] and B[i] != C[i] and C[i] != A[i]:
    ans += 2
  elif A[i] == B[i] != C[i] or A[i] != B[i] == C[i] or C[i] == A[i] != B[i]:
    ans += 1
  else:
    ans += 0
print(ans)