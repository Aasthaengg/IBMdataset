house = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]
n = int(raw_input())
for i in range(n):
  a = raw_input().split()
  house[int(a[0])-1][int(a[1])-1][int(a[2])-1] += int(a[3])
for i in range(4):
  if i != 0:
    print "#"*20
  for j in range(3):
    line = ""
    for k in range(10):
      line += " " + str(house[i][j][k])
    print line