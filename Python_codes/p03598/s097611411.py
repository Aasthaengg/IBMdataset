N = int(input())
K = int(input())
x = 0
arrayx = list()
if N == 1:
  x = int(input())
  if x <= (K - x):
    print(x * 2)
  else:
    print((K - x) * 2)
  exit(0)
else:
  arrayx = list(map(int,input().split()))

sum = 0
for i in range(N):
  if arrayx[i] <= (K - arrayx[i]):
    sum += arrayx[i] * 2
  else:
    sum += (K - arrayx[i]) * 2
print(sum)