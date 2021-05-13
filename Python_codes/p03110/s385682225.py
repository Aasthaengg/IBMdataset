Row = int(input())
List = []
for i in range (Row):
  List.append(list(map(str, input().split())))
res = 0
for i in range(Row):
  if List[i][1] == "JPY":
    res += float(List[i][0])
  else:
    res += float(List[i][0])*380000
print(res)