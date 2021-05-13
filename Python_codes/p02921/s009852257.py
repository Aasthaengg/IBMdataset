A = input()
B = input()
ans = 0
for i in range(3):
  if A[i] == B[i]:
    ans += 1
print(ans)