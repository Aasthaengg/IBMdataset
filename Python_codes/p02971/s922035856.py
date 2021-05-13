N=int(input())
l=[]
l.append(int(input()))
l.append(int(input()))
m1=max(l)
m2=min(l)
for _ in range(N-2):
  l.append(int(input()))
  if l[-1] >= m1:
    m2 = m1
    m1 = l[-1]
  elif l[-1] > m2:
    m2 = l[-1]
for i in range(N):
  if l[i] == m1:
    print(m2)
  else:
    print(m1)