N,M=map(int,input().split())
List = []
for i in range (M):
  List.append(list(map(int, input().split())))
resList = [0]*N
for i in range(M):
  resList[List[i][0]-1] +=1
  if List[i][1]<N:
    resList[List[i][1]] +=-1
for j in range(1,N):
  resList[j] = resList[j] + resList[j-1]
print(resList.count(M))