r, c = (int(i) for i in input().split())
table = tuple([int(x) for x in input().split()] for _ in range(r))
for cols in table:
  cols.append(sum(cols))
  print(*cols)
else:
  sums = tuple(sum(table[y][x] for y in range(r)) for x in range(c + 1))
  print(*sums)