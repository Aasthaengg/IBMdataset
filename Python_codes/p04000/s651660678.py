h,w,n = map(int,input().split())
coord = [list(map(int,input().split())) for i in range(n)]

num = {}

for i in range(n):
  for j,k in [[0,0],[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]:
    if not(2<=coord[i][0]+j<=h-1) or not(2<=coord[i][1]+k<=w-1):
      continue
    if not coord[i][0]+j in num:
      num[coord[i][0]+j] = {}
    if not coord[i][1]+k in num[coord[i][0]+j]:
      num[coord[i][0]+j][coord[i][1]+k] = 1
    else:
      num[coord[i][0]+j][coord[i][1]+k] += 1

ans = [0]*10
for i in num:
  for value in num[i].values():
    ans[value] +=1

print((h-2)*(w-2)-sum(ans))
for i in range(1,10):
  print(ans[i])