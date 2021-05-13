s = str(input()); n = len(s)
gx,gy = map(int,input().split())
Yoko = []; Tate = []
Flag = 0; cnt = 0
Max_x = 0; Max_y = 0
for i in range(n):
  if s[i] == "F":
    cnt += 1
    if i == n-1: #最後なら登録
      if Flag == 0:
        Max_x += cnt
        Yoko.append(cnt)
      else:
        Max_y += cnt
        Tate.append(cnt)      
  else: #T
    if Flag == 0:
      Max_x += cnt
      Yoko.append(cnt)
    else:
      Max_y += cnt
      Tate.append(cnt)
    cnt = 0
    Flag = Flag^1
#print(Yoko,Tate)
MAX_dpx = Max_x*2+1
dp = [0 for _ in range(MAX_dpx)]
dp[Max_x] = 1

for i,x in enumerate(Yoko):
  p = [0 for _ in range(MAX_dpx)]
  p,dp = dp,p
  for j in range(MAX_dpx):
    if i == 0: #i=0の時は右向きだけ
      if 0<=j+x<MAX_dpx:
        dp[j+x] = max(dp[j+x], p[j])
    else:
      if 0<=j+x<MAX_dpx:
        dp[j+x] = max(dp[j+x], p[j])
      if 0<=j-x<MAX_dpx:
        dp[j-x] = max(dp[j-x], p[j])
  #print(dp)
#print(dp)
#print(gx+Max_x,MAX_dpx)
if gx+Max_x >= MAX_dpx or gx+Max_x < 0 or dp[gx+Max_x] == 0:
  print("No");exit()

MAX_dpy = Max_y*2+1
dp = [0 for _ in range(MAX_dpy)]
dp[Max_y] = 1

for i,y in enumerate(Tate):
  p = [0 for _ in range(MAX_dpy)]
  p,dp = dp,p
  for j in range(MAX_dpy):
    if 0<=j+y<MAX_dpy:
      dp[j+y] = max(dp[j+y], p[j])
    if 0<=j-y<MAX_dpy:
      dp[j-y] = max(dp[j-y], p[j])
  #print(dp)
#print(dp)
if gy+Max_y >= MAX_dpy or gy+Max_y < 0 or dp[gy+Max_y] == 0:
  print("No")
else:
  print("Yes")