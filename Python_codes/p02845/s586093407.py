n = int(input())
A = list(map(int, input().split()))
x = 0
y = 0
z = 0
ans = 1
for i in range(n):
  a = A[i]
  ans *= int(a==x) + int(a==y) + int(a==z)
  if a == x:
    x += 1
  elif a == y:
    y += 1
  elif a == z:
    z += 1
  else:
    print(0)
    exit()
print(ans%(10**9+7))