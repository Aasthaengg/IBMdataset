n = int(input())
for i in range(1000):
  if n % 111 == 0:
    print(n)
    exit()
  n += 1