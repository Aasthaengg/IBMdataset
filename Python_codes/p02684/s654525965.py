N, K = map(int, input().split())
A = list(map(int, input().split()))

X = 0
town = 1
counted = [0 for _ in range(N)]
List = [0 for _ in range(N)]
for k in range(N):
  X += 1
  counted[k] = town
  town = A[town-1]
  if List[town-1] == 1:
    ini = counted.index(town)
    Q = X - ini
    break
  else:
    List[town-1] = 1
if K >= ini:    
  num = (K-ini) % Q
  print(counted[ini+num])
else:
  print(counted[K])