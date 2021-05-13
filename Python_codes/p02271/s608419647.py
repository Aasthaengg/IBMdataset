memo = {}
def solve(p, t):
  key = "{}:{}".format(p, t)
  if key in memo: return memo[key]
  if p >= len(A): return False
  if t == A[p]: return True
  if t <= 0: return False
  #print("({}, {})".format(p, t))

  if solve(p + 1, t):
    memo["{}:{}".format(p + 1, t)] = True
    return True
  else:
    memo["{}:{}".format(p + 1, t)] = False
    return solve(p + 1, t - A[p])

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

for t in M:
  if solve(0, t): print("yes")
  else: print("no")