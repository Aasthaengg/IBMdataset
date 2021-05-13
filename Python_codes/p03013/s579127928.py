patterns = [None] * (10**5 + 10)
patterns[0] = 1
patterns[1] = 1
calcurated_until = 1
MOD = 10**9+7
def get_patterns(n):
  global calcurated_until, patterns
  if patterns[n] is None:
    for i in range(calcurated_until + 1, n + 1):
      patterns[i] = (patterns[i-1] + patterns[i-2])%MOD
    calcurated_until = n
  #print('p', n, patterns[n])
  return patterns[n]

def solve():
  N, M = map(int, input().split())
  A = [-1]
  for _ in range(M):
    A.append(int(input()))
  A.append(N+1)
  #print(A)
  
  ans = 1
  for a1, a2 in zip(A[:-1], A[1:]):
    #print(a1, a2)
    if a2 == a1+1:
      print('0')
      return
    #print('ans', ans)
    #print('get_patterns(a2 - a1 - 2)', get_patterns(a2 - a1 - 2))
    ans *= get_patterns(a2 - a1 - 2)
    #print('ans', ans)
    ans %= MOD
    #print('ans', ans)
  print(ans)
solve()
