from heapq import heappush, heappop
N, K = map(int, input().split())
A = [int(i) for i in input().split()]
x = sum(A)
ls = []
for i in range(1, int(x**0.5)+1):
  if x%i==0:
    ls += [i]
    if i != x//i:
      ls += [x//i]
ls.sort(reverse=True)
for i in ls:
  B =[]
  for j in A:
    heappush(B, -1*(j%i))
  y = sum(B)
  while y<0:
    u = heappop(B)
    u += i
    heappush(B,u)
    y += i
  m = 0
  for j in B:
    if j>0:
      m += j
  if m>K:
    continue
  else:
    print(i)
    break
