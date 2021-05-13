n = int(input())

# boss[m] = b.  member m has boss b
boss = [int(i) - 1 for i in input().split()]

sub = { i: 0 for i in range(n) }
for b in boss:
  sub[b] += 1

for m in range(n):
  print(sub[m])

