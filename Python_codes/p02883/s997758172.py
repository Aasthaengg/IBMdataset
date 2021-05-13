import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
A = sorted(list(map(int,readline().split())))
F = sorted(list(map(int,readline().split())),reverse = True)

ok = A[-1] * F[0]
ng = -1

def isOk(x):
  # 時間がxになるためには、A_iをx/F_i以下まで減らす必要がある
  diff = 0
  for i in range(len(A)):
    diff += max(A[i] - x // F[i], 0)
  return diff <= K
  
while (ok - ng)>1:
  mid = (ok + ng) // 2
  if isOk(mid):
    ok = mid
  else:
    ng = mid
print(ok)