n, m, l = map(int, input().split())

AL = []
for i in range(n):
 ail = list(map(int,input().split()))
 AL.append(ail)

BL = []
for i in range(m):
 bil = list(map(int,input().split()))
 BL.append(bil)

for i in range(n):
 for j in range(l - 1):
  CI = 0
  for k in range(m):
   CI += AL[i][k] * BL[k][j]
  print(str(CI) + " ", end="")
 CI = 0
 for k in range(m):
  CI += AL[i][k] * BL[k][-1]
 print(str(CI))