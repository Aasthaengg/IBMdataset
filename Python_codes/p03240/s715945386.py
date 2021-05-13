N = int(input()); INF = float("inf")
Z = []
S = set([])
for i in range(N):
  x,y,h = map(int,input().split())
  Z.append((x,y,h))
  S.add((x,y))
Z.sort(key=lambda x : x[2],reverse=True)
#print(Z)
for i in range(101):
  for j in range(101):
    #Flag = True #0以外があればFalse
    MAX = INF
    for t in range(N):
      #print(Z[t][2])
      if t == 0: #最初は必ず0以外。
        ans = abs(i-Z[t][0])+abs(j-Z[t][1])+Z[t][2]
      elif Z[t][2] == 0:
        MAX = min(MAX,abs(i-Z[t][0])+abs(j-Z[t][1])+Z[t][2])
      else:
        temp = abs(i-Z[t][0])+abs(j-Z[t][1])+Z[t][2]
        if temp != ans:
          break
      if t != N-1: #最後じゃないなら続く。
        continue
      #print(i,j,MAX,ans)
      if ans <= MAX:
        ret = [i,j,ans]
        print(*ret);exit()
      else:
        break
      
