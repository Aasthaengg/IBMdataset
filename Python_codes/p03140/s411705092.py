N = int(input())
A = input()
B = input()
C = input()
r = 0
for i in range(N):
  a, b, c = A[i], B[i], C[i]
  if a == b == c:
    continue
  elif a == b or b == c or c == a:
    r += 1
  else:
    r += 2
print(r)
