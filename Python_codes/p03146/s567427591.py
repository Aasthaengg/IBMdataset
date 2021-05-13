def func(n):
  return int((n / 2) if n % 2 == 0 else (3 * n + 1))

s = int(input())

A = [s]
i = 0
while A[i] not in A[:i]:
  A.append(func(A[i]))
  i += 1
print(i + 1)