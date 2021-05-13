N = int(input())
map_T = map(int, input().split())
list_T = list(map_T)
M = int(input())
sumtime = sum(list_T)

for i in range(M):
  map_PX = map(int, input().split())
  list_PX = list(map_PX)
  sumtime_drink = sumtime- list_T[list_PX[0]- 1]+ list_PX[1]
  print(sumtime_drink)