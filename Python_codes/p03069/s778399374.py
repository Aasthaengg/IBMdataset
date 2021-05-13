n = int(input())
s = input()
A = []
for si in s:
  if si == "#":
    A.append(1)
  else:
    A.append(0)
for i in range(1, len(A)):
  A[i] += A[i-1]

ans = n - A[n-1]
for i in range(n):
  b2w = A[i]
  w2b = n - i - 1 - (A[n-1] - A[i])
  if ans > b2w + w2b:
    ans = b2w + w2b

print(ans)

