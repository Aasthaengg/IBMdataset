s = input()
x, y = list(map(int, input().split()))
Ans = ["No", "Yes"]
UD = []
RL = []
ud = 0
rl = 0
f = -1
cnt = 0
for i in s:
  if i == "F":
    cnt += 1
  else:
    if f == 0:
      UD.append(cnt)
      ud += cnt
      f = 1
    elif f == 1:
      RL.append(cnt)
      rl += cnt
      f = 0
    else:
      f = 0
      x -= cnt
    cnt = 0

if f == 0:
  UD.append(cnt)
  ud += cnt
elif f == 1:
  RL.append(cnt)
  rl += cnt
else:
  x -= cnt

if abs(y) > ud or abs(x) > rl:
  print(Ans[0])
  exit()

d = ud - abs(y)
l = rl - abs(x)

if d % 2 == 1 or l % 2 == 1:
  print(Ans[0])
  exit()

if d != 0:
  memo = [0]
  k = d // 2
  for i in UD:
    t = [0]
    for j in memo:
      if i + j == k:
        break
      if i + j < k:
        t.append(i + j)
    else:
      memo = t
      continue
    break
  else:
    print(Ans[0])
    exit()

if l != 0:
  memo = [0]
  k = l // 2
  for i in RL:
    t = [0]
    for j in memo:
      if i + j == k:
        break
      if i + j < k:
        t.append(i + j)
    else:
      memo = t
      continue
    break
  else:
    print(Ans[0])
    exit()

print(Ans[1])