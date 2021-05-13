List = list(map(int, input().split()))
List.sort()
res = 10 * List[2] + List[0]+List[1]
print(res)