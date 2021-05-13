N = int(input())
A = list(map(int,input().split()))

A.sort()
stack = A[1:]
m = A[0]

while stack:
  stack = list(stack)
  l = []
  for x in stack:
    if x % m == 0:
      continue
    l.append(x % m)
  
  if not l:
    break
  l.append(m)
  m = min(l)
  stack = set(l)

print(m)
