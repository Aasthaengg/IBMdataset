W,H,N=map(int,input().split())
List = []
for i in range (N):
  List.append(list(map(int, input().split())))
WRange = [0,W]
HRange = [0,H]
for i in range(N):
  if List[i][2] == 1:
    WRange[0] = max(WRange[0],List[i][0])
  elif List[i][2] == 2:
    WRange[1] = min(WRange[1],List[i][0])
  elif List[i][2] == 3:
    HRange[0] = max(HRange[0],List[i][1])
  else:
    HRange[1] = min(HRange[1],List[i][1])
if WRange[1]-WRange[0] >0:
  W = WRange[1]-WRange[0]
else:
  W = 0
if HRange[1]-HRange[0] >0:
  H = HRange[1]-HRange[0]
else:
  H = 0
res = H * W
print(res)