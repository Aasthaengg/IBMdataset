n = int(input())
k = int(input())
ans = 1
while ans < k and n > 0:
  ans *= 2
  n -= 1
print(ans + k * n)  