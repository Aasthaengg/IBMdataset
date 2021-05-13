N=int(input())
count = 0
sum = 0
while N != 0:
  count += 2**sum
  sum += 1
  N = int(N/2)
print(count)