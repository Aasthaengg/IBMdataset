N = int(input())
ListP = []
for i in range (N):
  ListP.append(input())
M = int(input())
ListN = []
for i in range (M):
  ListN.append(input())
res = 0
mid = 0
for i in range(N):
  mid += ListP.count(ListP[i])
  mid += -ListN.count(ListP[i])
  res = max(res,mid)
  mid = 0
print(res)