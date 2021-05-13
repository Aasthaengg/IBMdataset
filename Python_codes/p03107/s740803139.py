s = input()
n = len(s)
ones = 0
for i in s:
  if i == '1':
    ones += 1
print(min(ones, n - ones) * 2)