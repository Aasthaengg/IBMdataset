a=int(input())
List1 = list(map(int, input().split()))
Row = int(input())
List2 = []
for i in range (Row):
  List2.append(list(map(int, input().split())))
res = [0]*Row
for i in range(Row):
  for j in range(a):
    if j+1 == List2[i][0]:
      res[i] += List2[i][1]
    else:
      res[i] += List1[j]
for element in res:
  print(element)