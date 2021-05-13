d = input().split()
p = [(-1, 2, 4, 1, 3, -1), (3, -1, 0, 5, -1, 2), (1, 5, -1, -1, 0, 4),
(4, 0, -1, -1, 5, 1), (2, -1, 5, 0, -1, 3), (-1, 3, 1, 4, 2, -1)]
for _ in range(int(input())):
  t, f = [d.index(s) for s in input().split()]
  print(d[p[t][f]])
