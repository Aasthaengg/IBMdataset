def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

N,M=MI()
SC=[tuple(map(int,input().split())) for _ in range(M)]
def check(n):
  n=str(n)
  if len(n)!=N:
    return False
  for i in range(M):
    if n[SC[i][0]-1]!=str(SC[i][1]):
      return False
  return True

for i in range(1000):
  if check(i):
    print(i)
    exit()
else:
   print(-1)