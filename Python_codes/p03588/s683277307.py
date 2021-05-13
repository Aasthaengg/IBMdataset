n = int(input())
max_value = -1
diff_between_0 = 0

for _ in range(n):
  a, b = [int(x) for x in input().split()]
  if max_value < a:
    max_value = a
    diff_between_0 = b

print(max_value + diff_between_0)