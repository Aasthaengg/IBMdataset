import collections

N = int(input())
Ds = list(map(int, input().split()))
M = int(input())
Ts = list(map(int, input().split()))

Ds = collections.Counter(Ds)
Ts = collections.Counter(Ts)

if N < M:
  print('NO')
  exit()
  
for k in Ts:
  if Ts[k] > Ds[k]:
    print('NO')
    exit()

print('YES')