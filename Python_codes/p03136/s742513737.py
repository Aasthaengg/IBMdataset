N=int(input())
List = list(map(int, input().split()))
List.sort()
wa = 0
for i in range(N-1):
  wa += List[i]
if List[N-1] < wa:
  print("Yes")
else:
  print("No")