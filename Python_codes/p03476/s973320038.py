#-----------------------------------
#リストera_list[n]を返す
#0～ｎの各インデックスが素数であれば1、そうでなければ0
#ex：eratosthenes(10)
#　　→ [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
#-----------------------------------

def eratosthenes(n):
  era_list = [1] * (n + 1)
  era_list[0] = 0; era_list[1] = 0
  
  for i in range(2,n+1):
    if era_list[i] == 0:
      continue
    else:
      j = i + i
      while j <= n:
        era_list[j] = 0
        j += i
        
  return era_list

Q = int(input())
PN = eratosthenes(100001)
TF = [0] * 100001

for i in range(1,100001,2):
  if PN[i] == 1 and PN[int((i+1)/2)] == 1:
    TF[i] = 1 + TF[i-2]
  else:
    TF[i] = TF[i-2]
    
for j in range(1,Q+1):
  l,r = map(int, input().split())
  Ans = TF[r] - TF[l-2]
  print(Ans)