n,x = map(int,input().split())
l = list(map(int,input().split()))
cnt = 1
t = 0
for v in l:
  t += v
  if t>x:
    break
  cnt += 1
print(cnt)