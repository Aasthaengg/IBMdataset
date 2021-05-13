N, M = map(int, input().split())

ans = []
neg = 0
for n in range(N):
  ans.append(-1)

for m in range(M):
  s, c = map(int, input().split())
  if ans[s-1] == -1:
    ans[s-1] = c
  elif ans[s-1] == c:
    pass
  else:
    neg = -1
    break

if ans[0] == 0 and N != 1:
  neg = -1

for j in range(len(ans)):
  if ans[j] == -1:
    ans[j] = 0

if N == 1:
  pass

elif ans[0] == 0:
  ans[0] = 1

if neg == -1:
  print(neg)
else:
  print("".join([str(i) for i in ans]))