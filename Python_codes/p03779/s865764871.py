X = int(input())

def f(n):
  return n*(n+1) // 2

n = 0
for i in range(1, X+1):
  if f(i) >= X:
    n = i
    break

print(n)