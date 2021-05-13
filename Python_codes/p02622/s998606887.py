s, t = [input() for i in range(2)]
i = 0
for a, b in zip(s, t):
  if a != b:
    i += 1
print(i)