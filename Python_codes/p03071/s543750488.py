List = list(map(int, input().split()))
List.sort()
res = 0
for i in range(2):
  a= List.pop(1)
  res += a
  List.append(a-1)
  List.sort()
print(res)