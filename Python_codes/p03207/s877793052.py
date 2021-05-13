N = int(input())

max = 0
sum = 0
for n in range(N):
  x = int(input())
  if max < x:
    max = x
  sum += x
print(sum-max//2)