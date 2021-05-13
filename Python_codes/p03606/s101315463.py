Row = int(input())
List = []
for i in range (Row):
  List.append(list(map(int, input().split())))
res=0
for i in range(Row):
  res += List[i][1]-List[i][0]+1
print(res)