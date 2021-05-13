n = int(input())

for i in range(1000):
  if 100*i<=n and 105*i>=n:
    print("1")
    exit()
print("0")