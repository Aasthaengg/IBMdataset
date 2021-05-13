a=int(input())
List = list(map(int, input().split()))
List.sort()
res = List[a-1]-List[0]
print(res)