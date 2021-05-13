n = int(input())
lucas = [2, 1] + [0] * (n - 1)
for i in range(2, n + 1):
  lucas[i] = lucas[i - 1] + lucas[i - 2]
print(lucas[n])