N = int(input())

dic = {(i,j):set([]) for i in range(1,N+1) for j in range(2)}

for i in range(1,N+1):
  a = int(input())
  for _ in range(a):
    x,y = map(int, input().split())
    dic[(i,y)].add(x)
    
p = 2**N
rlt = 0

for b in range(p):
  s0 = set([])
  s1 = set([])
  for i in range(N):
    if b&(1<<i):
      s1.add(i+1)
    else:
      s0.add(i+1)
  f = 1
  for i in s1:
    for k in dic[(i,1)]:
      if k in s0:
        f = 0
        break
    for k in dic[(i,0)]:
      if k in s1:
        f = 0
        break
    if f == 0:
      break
  if f == 1:
    rlt = max(len(s1),rlt)
    
print(rlt)