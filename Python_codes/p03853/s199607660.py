H,W=map(int,input().split())
List = []
for i in range (H):
  a=input()
  List.append(list(a))
New_List=[]
for i in range(H):
  New_List.append(List[i])
  New_List.append(List[i])
res = ""
for i in range(2*H):
  for j in range(W):
    res += New_List[i][j]
  print(res)
  res = ""