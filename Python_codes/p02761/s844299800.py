N,M=map(int,input().split())
flag = True
res = ""
List = []
for i in range (M):
  List.append(list(map(int, input().split())))
resList = ["10"]*N
for i in range(M):
  if resList[List[i][0]-1] == "10":
    resList[List[i][0]-1] = str(List[i][1])
  else:
    if resList[List[i][0]-1] != str(List[i][1]):
      flag = False
if resList[0] == "0":
  flag = False
elif resList[0] == "10" and N > 1:
  resList[0]="1"
elif resList[0] == "10" and N == 1:
  resList[0]="0"
  flag = False
if flag:
  for i in range(N):
    if resList[i] == "10":
      res += "0"
    else:
      res += resList[i]
  print(int(res))
else:
  if resList[0] == "0" and N ==1:
    print(0)
  else:
    print(-1)