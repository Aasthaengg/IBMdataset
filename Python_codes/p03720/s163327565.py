N,M=map(int,input().split())
List = []
for i in range (M):
  List.append(list(map(int, input().split())))
resList = [0]*N
for i in range(M):
  resList[List[i][0]-1]+=1
  resList[List[i][1]-1]+=1
for element in resList:
  print(element)