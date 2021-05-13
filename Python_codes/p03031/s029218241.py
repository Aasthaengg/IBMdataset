n, m = map(int, input().split())
klst = []
for i in range(m):
  klst.append(list(map(lambda x: int(x) - 1, input().split()))[1:])
plst = list(map(int, input().split()))
res = 0
for ibit in range(2 ** n):
  TF = True
  for j in range(m):
    cnt = 0
    for swnum in klst[j]:
      if ((ibit >> swnum) & 1):
        cnt += 1
    if cnt % 2 != plst[j]:
      TF = False
  if TF:
    res += 1
print(res)