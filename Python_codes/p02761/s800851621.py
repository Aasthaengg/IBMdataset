N, M = map(int, input().split())
lis = {}
if N == 1 and M == 0:
  print(0)
  exit()
if N == 2 and M == 0:
  print(10)
  exit()
if N == 3 and M == 0:
  print(100)
  exit()
if N == 1 and M == 1:
  s, c = map(int, input().split())
  print(c)
  exit()
for i in range(M):
  s, c = map(int, input().split())
  if s == 1 and c == 0:
    print(-1)
    exit()
  if s in lis:
    if lis[s] == c:
      continue
    else:
      print(-1)
      exit()
  else:
    lis[s] = c
if not 1 in lis:
  lis[1] = 1
for i in range(2, N+1):
  if not i in lis:
    lis[i] = 0
ans = ""
for i in range(1, N+1):
  ans += str(lis[i])
print(ans)