N=int(input())
List = list(map(int, input().split()))
res = 0
for i in range(N-2):
  if List[i] < List[i+1] and List[i+1] < List[i+2]:
    res += 1
  elif List[i] > List[i+1] and List[i+1] > List[i+2]:
    res += 1
print(res)