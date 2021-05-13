s = input()
t = input()

result = 0
for i, c in enumerate(s):
  if c != t[i]:
    result += 1
print(result)