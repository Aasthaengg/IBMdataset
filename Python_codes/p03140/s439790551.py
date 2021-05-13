n = int(input())
A = input()
B = input()
C = input()
ans = 0
for i in range(n):
  if A[i] == B[i]:
    ans += 1
  if B[i] == C[i]:
    ans += 1
  if C[i] == A[i]:
    ans += 1
  if A[i] == B[i] == C[i]:
    ans -= 1
print(n*2-ans)
