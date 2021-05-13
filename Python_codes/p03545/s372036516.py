a = input()

for x in range(1<<3):
  s = a[0]

  for i in range(3):
    if x & (1<<i):
      s += '+'
    else:
      s += '-'
    s += a[i+1]

  if eval(s) == 7:
    print(s + '=7')
    exit()