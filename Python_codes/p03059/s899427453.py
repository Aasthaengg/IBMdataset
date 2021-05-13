A, B, T = list(map(int,input().split()))
count = 0
t = A
while t <= T + 0.5:
  count += B
  t += A
print(count)