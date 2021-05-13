n, m = map(int, input().split())
student = []
for i in range(n):
  student.append(tuple(map(int, input().split())))
point = []
for i in range(m):
  point.append(tuple(map(int, input().split())))
for i in range(n):
  dis = 10 ** 20
  idx = 0
  for j in range(m):
    temp = abs(student[i][0] - point[j][0]) + abs(student[i][1] - point[j][1])
    if temp < dis:
      dis = temp
      idx = j + 1
  print(idx)