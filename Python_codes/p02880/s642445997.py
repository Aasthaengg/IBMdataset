N = int(input())
n = 1
while n * n <= N:
  if N % n == 0 and N // n in range(1, 10):
    print('Yes')
    break
  n += 1
else:
  print('No')