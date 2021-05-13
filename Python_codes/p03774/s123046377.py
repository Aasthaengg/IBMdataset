a,b=map(int,input().split())
ListS = []
for i in range (a):
  ListS.append(list(map(int, input().split())))
ListP = []
for i in range (b):
  ListP.append(list(map(int, input().split())))
List = [100]*a
mid = 0
dist = 10000000000000000000
for i in range(a):
  for j in range(b):
    mid = abs(ListP[j][0]-ListS[i][0])+abs(ListP[j][1]-ListS[i][1])
    if dist > mid:
      dist = mid
      List[i] = j+1
    elif mid == dist:
      List[i] = min(List[i],j+1)
    else:
      pass
  dist = 10000000000000000000
for element in List:
  print(element)