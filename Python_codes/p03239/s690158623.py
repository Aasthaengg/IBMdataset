N,T=map(int,input().split())
List = []
for i in range (N):
  List.append(list(map(int, input().split())))
res = 1001
for i in range(N):
  if List[i][1] <= T:
    res = min(res,List[i][0])
if res == 1001:
  print("TLE")
else:
  print(res)