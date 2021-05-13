# Cx, Cyは0〜100の整数なので、101 * 101パターンを全探索

N=int(input())
data=[None] * N
for i in range(N):
  data[i] = list(map(int,input().split()))

for Cx in range(101):
  for Cy in range(101):
    H = -1
    for i in range(len(data)):
      if data[i][2]<1:
        continue
      H = data[i][2] + abs(data[i][0] - Cx) + abs(data[i][1] - Cy)
      break
    
    for i in range(len(data)):
      if data[i][2] != max(H - abs(data[i][0] - Cx) - abs(data[i][1] - Cy),0):
        break
    else:
      print(Cx,Cy,H)
      exit(0)
