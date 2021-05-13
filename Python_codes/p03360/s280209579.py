List = list(map(int, input().split()))
List.sort()
K=int(input())
for i in range(K):
  List[2] = List[2]*2
wa = 0
for i in range(3):
  wa += List[i]
print(wa)