n = int(input())
XLs = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    x = XLs[i][0]
    l = XLs[i][1]
    XLs[i].append(x+l) # 右腕の端の位置の情報を添える

XLs.sort(key=lambda x:x[2]) # 右腕の端の位置でソート

choice = -10**10 # 十分小さく(ロボの左腕の端の座標は最大でも -10*9)
cnt = 0
for i in range(n):
  x = XLs[i][0]
  l = XLs[i][1]
  if choice <= x-l: # 腕がかぶってるか判定
    choice = x+l
    cnt+=1 # 被っていなければ残す = カウント+1
print(cnt)