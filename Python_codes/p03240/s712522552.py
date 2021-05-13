N = int(input())
XYH = [list(map(int, input().split())) for i in range(N)]

XYH.sort(key=lambda x: x[2], reverse=True)

for x in range(101):
  for y in range(101):
    tmp_H = XYH[0][2]+abs(XYH[0][0]-x)+abs(XYH[0][1]-y)
    A = 0
    for i in range(1,N):
      if tmp_H - abs(XYH[i][0]-x) - abs(XYH[i][1]-y) == XYH[i][2]:
        A += 1
      elif tmp_H - abs(XYH[i][0]-x) - abs(XYH[i][1]-y) < 0 and XYH[i][2] == 0 :
        A += 1
    
    if A == N-1:
      print(x,y,tmp_H)