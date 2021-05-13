N=int(input())
List = list(map(int, input().split()))
res = 1
mini = List[0]
for i in range(1,N):
  if List[i] <= mini:
    res += 1
  mini = min(List[i],mini)
print(res)