from bisect import bisect_left,bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def is_ok(arg):
  L = bisect(A, arg)
  cnt = 0
  for i in range(L, N):
    p, q = divmod(A[i], arg)
    if q == 0:
      cnt += p-1
    else:
      cnt += p
  return cnt <= K

ng = 0
ok = max(A) + 1

def m_bisect(ng, ok):
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return ok

print(m_bisect(ng, ok))