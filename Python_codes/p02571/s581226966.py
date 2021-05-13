s = input()
t = input()

max_count = 0
for i in range(len(s) - len(t) + 1):
  count = 0
  for j in range(len(t)):
    if t[j] == s[i + j]:
      count += 1
  if max_count < count:
    max_count = count
print(len(t) - max_count)