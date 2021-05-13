N = int(input())

def num_divisors_table(n):
  table = [0] * (n + 1)
  for i in range(1, n + 1):
    for j in range(i, n + 1, i):
      table[j] += 1
  return table

table = num_divisors_table(1000000)

# a x b + c == n
# n - c == a x b

res = 0
for i in range(1, N):
  res += table[i]

print(res)