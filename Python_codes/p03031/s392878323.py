N,M=map(int,input().split())
combiList = []
for i in range (M):
  combiList.append(list(map(int, input().split())))
kakuninList = list(map(int, input().split()))
statusList = [0]*M

for j in range (M):
  combiList[j].pop(0)
res = 0
# 010 なら2番目のみ派閥 
for bits in range(2**N): #k番目のグループ
  flag = True
  statusList = [0]*M
  for j in range(N):
    if((bits>>j) & 1): 
      for k in range(M):
        if j+1 in combiList[k]:
          statusList[k] +=1
  for k in range(M):
    if statusList[k] % 2 != kakuninList[k]:
      flag = False
      break
  if flag:
    res +=1
print(res)