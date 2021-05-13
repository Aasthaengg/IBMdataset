N = int(input())
XYs = [[],[]]
for _ in range(N):
  x,y = map(int, input().split())
  XYs[0].append(x-y)
  XYs[1].append(x+y)
  
print(max(max(XYs[0])-min(XYs[0]), max(XYs[1])-min(XYs[1])))  
