N = int(input())
A = input()
B = input()
C = input()

ans = 0
for i in range(N):
  if A[i]!=B[i] and A[i]!=C[i] and B[i]!=C[i]:
    ans += 2
  elif A[i]!=B[i] or A[i]!=C[i] or B[i]!=C[i]:
    ans += 1
print(ans)