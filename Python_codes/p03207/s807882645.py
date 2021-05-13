Row = int(input())
List = []
res = 0
for i in range (Row):
  List.append(int(input()))
List.sort()
List[Row-1] = List[Row-1]//2
for i in range (Row):
  res += List[i]
print(res)