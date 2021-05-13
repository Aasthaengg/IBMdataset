a, b = map(int, input().split())

table = []

whites = 1
blacks = 1

# black bg, white holes
for i in range(50):
  table += [[]]
  if i % 2 == 1:
    table[i] = ['#' for i in range(100)]
    continue
  
  for j in range(100):
    if whites < a and j % 2 == 0:
      table[i] += ['.']
      whites += 1
    else:
      table[i] += ['#']
  
  if whites >= a:
    break

table += [['#' for i in range(100)]]

parity = len(table) % 2
for i in range(len(table), 100):
  table += [[]]
  if i % 2 == parity:
    table[i] = ['.' for i in range(100)]
    continue

  for j in range(100):
    if blacks < b and j % 2 == 0:
      table[i] += ['#']
      blacks += 1
    else:
      table[i] += ['.']
  
  if blacks >= b:
    break

print(len(table), 100)
for i in range(len(table)):
  print("".join(table[i]))