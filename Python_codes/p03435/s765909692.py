c = []
c.append([int(i) for i in input().split()])
c.append([int(i) for i in input().split()])
c.append([int(i) for i in input().split()])

for i in range(2):
  c0 = c[0][i] - c[0][i + 1]
  c1 = c[1][i] - c[1][i + 1]
  c2 = c[2][i] - c[2][i + 1]
  if not (c0 == c1 == c2):
    print("No")
    exit(0)


for i in range(2):
  r0 = c[i][0] - c[i + 1][0]
  r1 = c[i][1] - c[i + 1][1]
  r2 = c[i][2] - c[i + 1][2]
  if not (c0 == c1 == c2):
    print("No")
    exit(0)

print("Yes")

