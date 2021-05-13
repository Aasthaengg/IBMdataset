N = int(input())

for i in range(N, 0, -1):
  if (i ** (1/2)) % 1 == 0:
    print(i)
    exit()