N, K = map(int, input().split())
S = list(map(int, input()))

prev = S[0]
renzoku_start = [0]
for i in range(1, N):
  if prev == S[i]:
    continue
  else:
    prev = S[i]
    renzoku_start.append(i)
renzoku_start.append(N)

ans = []
l = len(renzoku_start)
for j in range(l):
  if S[renzoku_start[j]] == 0:
    if j + 2 * K >= l:
      ans.append(N - renzoku_start[j])
      break
    ans.append(renzoku_start[j + 2 * K] - renzoku_start[j])
  else:
    if j + 2 * K + 1 >= l:
      ans.append(N - renzoku_start[j])
      break
    ans.append(renzoku_start[j + 2 * K + 1] - renzoku_start[j])

if ans:
  print(max(ans))
else:
  print(N)