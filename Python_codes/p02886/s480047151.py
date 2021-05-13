N=int(input())
List = list(map(int, input().split()))
wa = 0
for i in range(N):
  for j in range(N):
    if j == i:
      pass
    else:
      wa += List[i]*List[j]
wa = wa //2
print(wa)