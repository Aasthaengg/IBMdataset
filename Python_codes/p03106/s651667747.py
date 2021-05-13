A, B, K = map(int, input().split())
i, t = 101, 1
while t<=K:
  i -= 1
  if A%i==0 and B%i ==0:
    t += 1
print(i)