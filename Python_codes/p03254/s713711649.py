N, x = map(int,input().split())

al = list(map(int,input().split()))

al.sort()

cnt = 0

for a in al[:N-1]:
  if x >= a:
    x -= a
    cnt += 1
  else:
    break
if al[-1] == x:
  cnt += 1

print(cnt)