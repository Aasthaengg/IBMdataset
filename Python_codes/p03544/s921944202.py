N = int(input())

a = 2
b = 1
ans = 0

if N == 1:
  ans = 1
else:
  for i in range(N-1):
    b, a = a + b, b
    ans = b

print(ans)
