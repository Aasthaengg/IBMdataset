a, b = [int(num) for num in input().split()]
sum = 0

if a < b or a == b:
  sum = a
else:
  sum = a - 1
print(sum)