H,W = map(int,input().split())
S = []
for i in range(H):
  S.append(input())

m = [[0 for i in range(W)] for j in range(H)]
#yoko
for i in range(H):
  s = S[i]
  mar = 0
  cnt = 0
  for j in range(W):
    if s[j] == ".":
      cnt += 1
    if s[j] == "#":
      for k in range(mar,j):
        m[i][k] += cnt
      cnt = 0
      mar = j+1    
    #グリッドの端の処理
    if j == W-1 and s[j] == ".":
      for k in range(mar,j+1):
        m[i][k] += cnt


#tate      
for i in range(W):
  mar = 0
  cnt = 0
  for j in range(H):
    if S[j][i] == ".":
      cnt += 1
    if S[j][i] == "#":
      for k in range(mar,j):
        m[k][i] += cnt
      cnt = 0
      mar = j+1 
    #グリッドの端の処理
    if j == H-1 and S[j][i] == ".":
      for k in range(mar,j+1):
        m[k][i] += cnt


ans = 0
for i in range(H):
  ans = max(ans,max(m[i]))
print(ans-1)  