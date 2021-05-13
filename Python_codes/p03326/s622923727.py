N, M = map(int,input().split())

L = []
S = []
for i in range(N):
  temp = list(map(int,input().split()))
  L.append(temp)
  TL = []
  TL.append(temp[0]+temp[1]+temp[2])
  TL.append(-1*temp[0]+temp[1]+temp[2])
  TL.append(temp[0]-temp[1]+temp[2])
  TL.append(temp[0]+temp[1]-temp[2])
  TL.append(-1*temp[0]-temp[1]+temp[2])
  TL.append(-1*temp[0]+temp[1]-temp[2])
  TL.append(temp[0]-temp[1]-temp[2])
  TL.append(-1*temp[0]-temp[1]-temp[2])
  S.append(TL)

ans = -float('inf') 
for i in range(8):
  TMP = []
  for j in range(N):
    TMP.append(S[j][i])
  TMP.sort(reverse=True)
  ans = max(ans,sum(TMP[:M]))
  
print(ans)