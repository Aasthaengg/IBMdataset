# 0～7で5を作るには
# 0123467 5 7643210 5
# M = 1がxor sum = 0とならず例外

M,K = map(int,input().split())

def solve(M,K):
  if M == 0:
    if K == 0:
      return '0 0'
    else:
      return '-1'
  if M == 1:
    if K == 0:
      return '0 1 1 0'
    else:
      return '-1'
  U = 1<<M
  if K >= U:
    return -1
  other = [str(x) for x in range(U) if x != K]
  result = other + [str(K)] + other[::-1] + [str(K)]
  return ' '.join(result)

answer = solve(M,K)
print(answer)