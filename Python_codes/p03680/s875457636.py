Row = int(input())
List = []
for i in range (Row):
  List.append(int(input()))
s = 1
res = 0
flag = False
for i in range(Row):
  s = List[s-1]
  res += 1
  if s == 2:
    flag=True
    break
if not flag:
  print(-1)
else:
  print(res)