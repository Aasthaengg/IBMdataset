n,t = map(int, input().split())
CT = [list(map(int, input().split())) for i in range(n)]
C = []
for i in range(n):
  if CT[i][1] <= t:
    C.append(CT[i][0])
if all(CT[i][1] > t for i in range(n)) == True:
  print("TLE")
else:
  print(min(C))