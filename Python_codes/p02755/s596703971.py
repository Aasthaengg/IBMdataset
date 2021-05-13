A, B = map(int, input().split())

cand = [i for i in range(1, 1001)]
res = []
flg = False
for i in cand:
  if int(i * 0.08) == A and int(i * 0.10) == B:
    res.append(i)
    flg = True

if flg:
  print(res[0])
else:
  print(-1)