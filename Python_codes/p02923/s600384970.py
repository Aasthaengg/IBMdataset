N=int(input())
List = list(map(int, input().split()))
trial = 0
res = 0
for i in range(N-1):
  if List[i+1] <= List[i]:
    trial += 1
  else:
    res = max(res,trial)
    trial = 0
res = max(res,trial)
print(res)