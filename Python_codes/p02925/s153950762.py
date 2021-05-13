N = int(input())
es = [[] for i in range(N)]
cand = set()
for i in range(N):
  es[i] = [int(i)-1 for i in input().split()][::-1]
def check(i):
  if es[i]==[]:
    return
  j = es[i][-1]
  if es[j]==[]:
    return
  if es[j][-1]==i:
    cand.add(i)
    cand.add(j)

for i in range(N):
  check(i)
day = 0
while cand:
  day += 1
  precand = cand.copy()
  cand = set()
  for i in precand:
    x = es[i].pop()
  for i in precand:
    check(i)
for i in range(N):
  if len(es[i])!=0:
    print(-1)
    break
else:
  print(day)
