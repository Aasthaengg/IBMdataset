import sys
N = int(input())
l = []
for i in range(N):
  l.append(list(map(int,input().split())))

#Cx,Cyの探索
ansC = [0,0]
for i in range(0,100+1):
  for j in range(0,100+1):
    Cx = i
    Cy = j
    #Nこのデータから高さを決める
    for k in range(N):
      X,Y,h = l[k]
      c = 0
      if h >= 1:
        H = h + abs(X-Cx) + abs(Y-Cy)
        for k in range(N):
          X,Y,h = l[k]
          if h != max(H-abs(X-Cx)-abs(Y-Cy),0):
            break
          if k == N-1:  
            print(Cx,Cy,H)
            sys.exit()