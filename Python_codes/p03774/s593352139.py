N, M = map(int, input().split())
st = [list(map(int, input().split())) for _ in range(N)]
cp = [list(map(int, input().split())) for _ in range(M)]

def dis(st, cp):
  return abs(st[0] - cp[0]) + abs(st[1] - cp[1])

for n in range(N):
  min_dis = dis(st[n], cp[0])
  ans = 1
  for m in range(1, M):
    cur_dis = dis(st[n], cp[m])
    if cur_dis < min_dis:
      min_dis = cur_dis
      ans = m + 1
  print(ans)