N, M = map(int, input().split())
all = list(range(10**(N-1), 10**N))
if N == 1:
  all += [0]
# print(all)
for i in range(M):
  s, c = map(int, input().split())
  _all = []
  for j in all:
    k = str(j)[s-1]
    # print(k)
    if  int(k) == c:
      _all.append(j)
  all = _all
  if len(all) == 0:
    print(-1)
    exit()

print(min(all))
