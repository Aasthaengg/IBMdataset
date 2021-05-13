n, k = list(map(int, input().split()))

if n == 0:
  print(0)
  exit()

print(k * (k-1)**(n-1))