N = int(input())
aaa = []
for i in range(N):
  aaa.append(list(reversed(list(map(int, input().split())))))

cs = set(range(N))
for i in range(0, N*N+1):
  empty = True
  played = False
  ncs = set()
  for j in cs:
    aa = aaa[j]
    if len(aa) > 0:
      empty = False
      l = aa[-1]-1
      if j not in ncs and l not in ncs and len(aaa[l]) > 0 and aaa[l][-1] == j+1:
          aa.pop()
          aaa[l].pop()
          played = True
          ncs.add(j)
          ncs.add(l)
  cs = ncs
  if empty:
    print(i)
    break
  elif not played:
    print(-1)
    break