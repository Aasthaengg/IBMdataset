x = [0] * 5
for i in range(5):
  x[i] = int(input())

k = int(input())

ans = 0
for i in range(5):
  for j in range(5):
    if (x[i] - x[j]) > k:
      print(':(')
      exit(0)

print('Yay!')