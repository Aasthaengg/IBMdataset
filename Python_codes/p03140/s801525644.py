N = int(input())
A = input()
B = input()
C = input()
ans = 0
for i in range(N):
  a = {A[i], B[i], C[i]}
  if len(a) == 2:
    ans += 1
  if len(a) == 3:
    ans += 2
print(ans)