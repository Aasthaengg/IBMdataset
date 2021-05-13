N = int(input())
num = 0
if N % 2 == 0:
  num = N / 2
else:
  num = int(N / 2) + 1
print(num/N)