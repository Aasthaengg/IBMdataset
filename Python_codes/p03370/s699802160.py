Row,Mass=map(int,input().split())
List = []
for i in range (Row):
  List.append(int(input()))
wa = 0
for i in range(Row):
  wa += List[i]
List.sort()
Mass = Mass - wa
k = Mass // List[0] 
res = Row + k
print(res)