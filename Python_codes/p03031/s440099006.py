N, M = map(int, input().split())
K = []
for i in range(M):
  i = list(map(int, input().split()))
  K.append(i[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(2**N):
  tmp = i
  flag = True
  cnt = 0
  for j in range(len(K)):
    for k in range(N):
      if ((i>>k) & 1):
        if k+1 in K[j]:
          cnt += 1
    if cnt % 2 != p[j]:
      flag = False
      break
    else:
      cnt = 0
      i = tmp
  if flag:
    ans += 1
print(ans)