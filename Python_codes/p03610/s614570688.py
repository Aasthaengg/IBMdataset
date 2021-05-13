s = input()
res = ""
for i, s_i in enumerate(s):
  if i % 2 == 0:
    res += s_i
print(res)