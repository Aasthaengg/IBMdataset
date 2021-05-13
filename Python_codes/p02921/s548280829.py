a = input()
b = input()
s = 0
for a, b in zip(a, b):
  if a == b:
    s += 1
print(s)