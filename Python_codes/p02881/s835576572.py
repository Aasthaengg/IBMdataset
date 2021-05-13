N = int(input())
i = 1
X = 1
ans = N - 1
while X <= N:
  if N % i == 0:
    ans = i + (N // i) - 2
  X = X + i + i + 1
  i += 1
print(ans)
