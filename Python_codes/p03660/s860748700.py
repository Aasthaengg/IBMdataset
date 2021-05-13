N = int(input())
E = [set() for i in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  E[a].add(b)
  E[b].add(a)
DF = [-1]*N
q = [0]
DF[0] = 0
while q:
  c = q.pop()
  ns = E[c]
  for n in ns:
    if DF[n] < 0:
      DF[n] = DF[c]+1
      q.append(n)
#print(DF)
DS = [-1]*N
q = [N-1]
DS[N-1] = 0
while q:
  c = q.pop()
  ns = E[c]
  for n in ns:
    if DS[n] < 0:
      DS[n] = DS[c]+1
      q.append(n)
NF = 0
NS = 0
for i in range(N):
  if DF[i] <= DS[i]:
    NF += 1
  else:
    NS += 1
#print(NF, NS)
if NF > NS:
  print("Fennec")
else:
  print("Snuke")
