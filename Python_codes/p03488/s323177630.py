S = str(input())
N = len(S)
x,y = map(int,input().split())
X = []; Y =[]
Flag = True #Trueならx軸、Falseならy軸
seq = 0
for i in range(N):
  if S[i] == "T":
    if Flag:
      X.append(seq)
    if not Flag:
      Y.append(seq)
    Flag = not Flag
    seq = 0
  else:
    seq += 1
    if i == N-1:
      if Flag:
        X.append(seq)
      if not Flag:
        Y.append(seq)
#print(X,Y)
num = 8100 #真ん中
MAX = num*2+1
#X方向i回目でjにいる
dpx = [0 for _ in range(MAX)]
dpx[num] = 1
dpy = [0 for _ in range(MAX)]
dpy[num] = 1
for i in range(len(X)):
  px = [0 for _ in range(MAX)]
  px,dpx = dpx,px
  step = X[i]
  for j in range(MAX):
    if j -step >= 0:
      dpx[j] = max(dpx[j],px[j-step])
    if j + step < MAX and i != 0: #一番最初は左に戻れない
      dpx[j] = max(dpx[j],px[j+step])
for i in range(len(Y)):
  py = [0 for _ in range(MAX)]
  py,dpy = dpy,py
  step = Y[i]
  for j in range(MAX):
    if j -step >= 0:
      dpy[j] = max(dpy[j],py[j-step])
    if j + step < MAX:
      dpy[j] = max(dpy[j],py[j+step])
x += num;y+= num
#print(dpx)
#print(dpy)
if dpx[x] == 1 and dpy[y] == 1:
  print("Yes")
else:
  print("No")
  
      
     
