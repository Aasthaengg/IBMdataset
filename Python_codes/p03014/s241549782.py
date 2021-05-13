H, W = map(int, input().split())
HW = [0] * H
for i in range(H):
  HW[i] = str(input())
  
#縦  
T = [[0] * W for i in range(H)]  
for i in range(H):#4000000
  now = 0
  for j in range(W):
    if HW[i][j] == "#":
      T[i][j] = 0
      now = 0
    else:
      now += 1
      T[i][j] = now
      
  now = 0    
  for j in range(1, W + 1):
    if T[i][-j] == 0:
      now = 0
    elif now == 0:
      now = T[i][-j]
    else:
      T[i][-j] = now
    #print(i, now)  
  
#print(T)

#横
Y = [[0] * W for i in range(H)]  
for j in range(W):#4000000
  now = 0
  for i in range(H):
    if HW[i][j] == "#":
      Y[i][j] = 0
      now = 0
    else:
      now += 1
      Y[i][j] = now
      
  now = 0    
  for i in range(1, H + 1):
    if Y[-i][j] == 0:
      now = 0
    elif now == 0:
      now = Y[-i][j]
    else:
      Y[-i][j] = now
    #print(i, now)      
#print(Y)

ans = 0
for i in range(H):
  for j in range(W):
    if T[i][j] != 0 and Y[i][j] != 0:
      ans = max(ans, T[i][j] + Y[i][j] - 1)
      
print(ans)      
    
