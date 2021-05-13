N = int(input())
A = list(map(int, input().split()))
y = sum(A)
x = y * 1.0 / 2
s = 0
for i in range(N):
  s += A[i]
  if s >= x:
    break
print(min(abs(s - (y - s)), abs((s-A[i]) - (y - (s - A[i])))))