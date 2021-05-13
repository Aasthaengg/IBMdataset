k = int(input())
odd = 0
for i in range(1, k+1):
  if i%2==0:
    odd += 1
even = k - odd
print(even * odd)
