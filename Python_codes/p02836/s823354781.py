A = list(input())
i = 0
res = 0
while i < len(A) // 2:
  if A[i] != A[len(A) - 1 -i]:
    res += 1
  i += 1
print(res)