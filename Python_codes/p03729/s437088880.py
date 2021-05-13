line = input().split(' ')
if line[0][-1] == line[1][0] and line[1][-1] == line[2][0]:
  print("YES")
else:
  print("NO")