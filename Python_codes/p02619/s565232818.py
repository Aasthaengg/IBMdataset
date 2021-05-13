D=int(input())
ListC = list(map(int, input().split()))
dictC={}
for i in range (1,27):
   dictC[i] = int(0) 
ListS = []
for i in range (D):
   ListS.append(list(map(int, input().split())))
ListT = []
for i in range (D):
   ListT.append(int(input()))
res = 0
for j in range(D):
  res += ListS[j][ListT[j]-1]
  for i in range(1,27):
    if ListT[j] == i:
      pass
    else:
      res += -1*(j+1-dictC[i])*ListC[i-1]
  dictC[ListT[j]] = j+1
  print(res)