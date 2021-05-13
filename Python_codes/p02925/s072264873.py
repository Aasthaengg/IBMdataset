N = int(input())
A = [0 for i in range(N)]
for i in range(N):
  A[i] = [-1]+[int(c)-1 for c in input().split()][::-1]

def f(cand):
  can_use = []
  candl = set()
  for i in cand:
    c = A[i][-1]
    if A[c][-1]==i:
      can_use += [i]
  for n in can_use:
    A[n].pop()
    candl.add(n)
    if A[n][-1]!=-1:
      candl.add(A[n][-1])
  return len(can_use),candl

ans = 0
rest = N*(N-1)
cand = set(range(N))
while True:
  ans += 1
  x, cand = f(cand)
  if x==0:
    ans = -1
    break
  rest -= x
  if rest==0:
    break
print(ans)