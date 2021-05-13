N = int(input())
List = []
for i in range(N):
  List.append(list(map(str, input().split())))
Names = []
Points = []
for i in range(N):
  Names.append(List[i][0])
  Points.append(int(List[i][1]))
slName = set(Names)
NewName = list(slName)
NewName.sort()
Points.sort(reverse = True)
for i in range(len(NewName)):
  for j in range(len(Points)):
    for k in range(N):
      if List[k][0] == NewName[i] and int(List[k][1]) == Points[j]:
        print(k+1)
      else:
        pass