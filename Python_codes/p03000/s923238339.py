n, x = map(int, input().split())
cnt = 1
now = 0
for l in map(int, input().split()):
  now += l
  if now > x:
    break
  cnt += 1
print(cnt)