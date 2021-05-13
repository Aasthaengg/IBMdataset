List = list(map(int, input().split()))
List.sort()
res = List[2]-List[1]
List[1] = List[2]
List[0] += res
mid = List[2] - List[0]
if mid % 2 == 1:
  res += mid // 2 +2
else:
  res += mid //2
print(res)