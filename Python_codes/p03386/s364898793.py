A,B,K = map(int,input().split())
l = []
for i in range(A,A+K):
  if i > B:
    break
  l.append(i)

for i in range(B, B-K,-1):
  if i < A:
    break
  if not i in l:
    l.append(i)
l.sort()

for i in l:
  print(i)
