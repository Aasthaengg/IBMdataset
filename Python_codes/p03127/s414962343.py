n = int(input())
lst = list(map(int, input().split()))
for i in range(n - 1):
  a, b = min(lst[i], lst[i + 1]), max(lst[i], lst[i + 1]) # a < b
  while a != 0:
    a, b = b % a, a
  lst[i + 1] = b
print(lst[n - 1])