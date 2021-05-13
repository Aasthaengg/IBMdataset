s = input()
x = 0
for c in s:
  x += (1 if c == '+' else -1)
print(x)