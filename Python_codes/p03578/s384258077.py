n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))
dic = {}
for d in D:
  if d in dic:
    dic[d] += 1
  else:
    dic[d] = 1

flg = True
for t in T:
  if t in dic:
    if dic[t] == 0:
      flg = False
      break
    else:
      dic[t] -= 1
  else:
    flg = False
    break
if flg:
  print('YES')
else:
  print('NO')