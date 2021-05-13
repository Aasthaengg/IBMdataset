from collections import defaultdict
N = int(input())
dic = defaultdict(list)

for i in range(N-1):
  a, b  = map(int, input().split())
  dic[a-1] += [b-1]
  dic[b-1] += [a-1]

dist1 = [float('inf')]*N
dist2 = [float('inf')]*N

q1 = [0]
q2 = [N-1]

dist1[0] = 0
dist2[N-1] = 0

while q1:
  e = q1.pop()
  for p in dic[e]:
    if dist1[p]>dist1[e]+1:
      dist1[p] = dist1[e]+1
      q1 += [p]

while q2:
  e = q2.pop()
  for p in dic[e]:
    if dist2[p]>dist2[e]+1:
      dist2[p] = dist2[e]+1
      q2 += [p]

fennec = 0
snuke = 0
for i in range(N):
  if dist1[i]<=dist2[i]:
    fennec += 1
  else:
    snuke += 1
if fennec>snuke:
  print('Fennec')
else:
  print('Snuke')