s = input()

res = ''
for i, elem in enumerate(s):
  if i % 2 == 0:
    res += elem
print(res)