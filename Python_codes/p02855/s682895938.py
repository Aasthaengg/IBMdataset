H,W,K = map(int,input().split())
Cake = []
for i in range(H):
  temp = str(input())
  temp = list(temp)
  Cake.append(temp)
#print(Cake)

n = 0 #ケーキの番号
ans = [[0]*W for _ in range(H)]
rem = set([])
for i in range(H):
  row = set(Cake[i])
  if "#" not in row: #この列にイチゴがない。
    if i == 0 or i-1 in rem:
      rem.add(i) #上もない。
    else:
      ans[i] = ans[i-1]
  else:
    n += 1
    Flag = True #Trueの間は一個目のイチゴ
    for j in range(W):
      if Flag and Cake[i][j] == "#":
        ans[i][j] = str(n)
        Flag = False
      elif Cake[i][j] == "#":
        n += 1
        ans[i][j] = str(n)
      else:
        ans[i][j] = str(n)
    if rem:
      for t in rem:
        ans[t] = ans[i]
      rem = set([])
#print(ans)
for t in range(H):
  temp = " ".join(ans[t])
  print(temp)
#print(" ".join(ans[i]) for i in range(H))  