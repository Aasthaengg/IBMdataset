a, b, c, d = map(int, list(input()))
op = ['-', '', '+']
for i in range(0, 3, 2):
  for j in range(0, 3, 2):
    for k in range(0, 3, 2):
      if a + b*(i-1) + c*(j-1) + d*(k-1) == 7:
        print(f'''{a}{op[i]}{b}{op[j]}{c}{op[k]}{d}=7''')
        exit()