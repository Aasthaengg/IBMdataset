n = int(input())

total = 0
for j in range(1, n + 1):
  max_num = n // j
  total += (1 + max_num) * max_num * j // 2
print(total)