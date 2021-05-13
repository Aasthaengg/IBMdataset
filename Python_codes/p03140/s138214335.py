N = int(input())
A = input()
B = input()
C = input()
ans = 0
for i in range(N):
  if A[i] == B[i] == C[i]:
    continue
  elif A[i] == B[i] and B[i] != C[i]:
    ans += 1
  elif A[i] == C[i] and C[i] != B[i]:
    ans += 1
  elif B[i] == C[i] and C[i] != A[i]:
    ans += 1
  else:
    ans += 2
print(ans)