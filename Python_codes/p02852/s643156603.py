def ints():
  return [int(x) for x in input().split()]
def readi():
  return int(input())

N, M = ints()
N+=1
G=N-1
SUGOROKU = input()

if SUGOROKU[G]==1:
  print(-1)
  exit()

n = N-1
k = 0
tejun = []
while n>0:
  mmax = min(n, M)

  found = False
  for m in reversed(range(1, mmax+1)):
    if SUGOROKU[n-m]=='1':
      continue
    n -= m
    k += 1
    found = True
    tejun.append(m)
    break

  if not found:
    print(-1)
    exit()

print(*list(reversed(tejun)))
  

