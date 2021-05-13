N, M = map(int, input().split(' '))

On = [True for i in range(N)]
K = [0 for j in range(M)]
S = []

for j in range(M):
  inp = list(map(int, input().split(' ')))
  K[j] = inp[0]
  S.append(inp[1:])
  
P = list(map(int, input().split(' ')))


def check_condition(On, K, S, P):
  for j in range(len(K)):
    on_sum = 0
    for k in range(K[j]):
      if On[S[j][k]-1]: on_sum += 1
    if on_sum%2 != P[j]:
      return False
  return True

def enum_patterns(On, index, K, S, P):
  off = On.copy()
  off[index] = False
  if index == len(On)-1:
    count = check_condition(On, K, S, P) + check_condition(off, K, S, P)
  else:
    count = enum_patterns(On, index+1, K, S, P) + enum_patterns(off, index+1, K, S, P)
  return count


print(enum_patterns(On, 0, K, S, P))