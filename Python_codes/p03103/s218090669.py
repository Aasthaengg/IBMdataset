n, m = map(int, input().split())
AB = []
for i in range(n):
  abi = list(map(int, input().split()))
  AB.append(abi)
ABs = sorted(AB)
t = 0
ans = 0
for j in range(n):
  if m-t >= ABs[j][1]:
    t += ABs[j][1]
    ans += ABs[j][0]*ABs[j][1]
  else:
    ans += ABs[j][0]*(m-t)
    t += m-t
  if t == m:
    break
print(ans)
