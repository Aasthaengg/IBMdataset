s = input()

max_value = 0
count = 0
for c in s:
  if c in "ACGT":
    count += 1
  else:
    count = 0
  max_value = max(max_value, count)
print(max_value)