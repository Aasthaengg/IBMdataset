n = int(input())
a = []
b = []
for _ in range(n):
  A, B = map(int, input().split())
  a.append(A)
  b.append(B)
x = 0
for i in range(1, n+1):
  a[-i] += x
  if a[-i]%b[-i] != 0: x += b[-i] - a[-i]%b[-i]
print(x)