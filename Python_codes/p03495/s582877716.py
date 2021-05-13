N, K = map(int, input().split())
List = [0]*N
for a in map(int, input().split()):
  List[a-1] += 1
List.sort()
print(sum(l for l in List[:len(List)-K]))