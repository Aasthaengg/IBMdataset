N = str(input())

for i, c in enumerate(list(N)):
  if c==str(7):
    print('Yes')
    break
  elif i==len(N)-1:
    print('No')