N = int(input())
c = list(list(input()))

#仕切りの右側の赤石の数rr
#仕切りの左側の赤石の数rl
rr, rl = c.count("R"), 0

#全ての石の色が同じ場合
if rr == 0 or rr == N:
  print(0)
  exit()

#仕切りの右側の白石の数wr
#仕切りの左側の白石の数wl
wr, wl = N - rr, 0

for i in range(N + 1):
  if i == 0:
    ans = min(rr, wr)
    continue

  if c[i-1] == "R":
    rr -= 1
    rl += 1
  else:
    wr -= 1
    wl += 1

  if rr >= wl:
    ans = min(ans, rr)
  else: ans = min(ans, wl)

print(ans)