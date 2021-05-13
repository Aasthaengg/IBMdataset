n = list(input())
for i,v in enumerate(n):
  if v == '1':
    n[i] = '9'
  elif v == '9':
    n[i] = '1'
print("".join(n))