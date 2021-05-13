import math

N,A,B = map(int,input().split())
H = [int(input()) for _ in range(N)]
INF = 10**9
cnt = 0

def check(K):
  tmp = 0
  for i in range(N):
    rem = H[i] - B * K
    if rem > 0:
      tmp += math.floor((rem + (A - B - 1)) / (A - B))
  return tmp <= K

def binary_search(ok,ng):
  while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
      ok = mid
    else:
      ng = mid
  return ok

print(binary_search(INF,0))