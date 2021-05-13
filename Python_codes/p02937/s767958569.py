s = input()
t = input()
ans = 0
cur = 0
cnt = 0
for i in t:
  f = s.find(i, cur)
  if f == -1:
    cnt += 1
    f = s.find(i)
    if f == -1:
      print(-1)
      exit()
    else:
      cur = f + 1
  else:
    cur = f + 1
print(cur + len(s) * cnt)