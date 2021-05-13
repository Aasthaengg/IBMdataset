d = {
    'AC': 0,
    'WA': 0,
    'TLE': 0,
    'RE': 0,
}

for i in range(int(input())):
    d[input()] += 1

for i, v in d.items():
    print(f'{i} x {v}')
  
