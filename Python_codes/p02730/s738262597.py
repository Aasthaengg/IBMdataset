s = input()
n = len(s)
sformer = s[:int((n - 1) / 2)]
slatter = s[int((n + 1) / 2):]
if s == s[-1::-1] and sformer == sformer[-1::-1] and slatter == slatter[-1::-1]:
  print('Yes')
else:
  print('No')
