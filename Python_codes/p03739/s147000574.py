N = int(input())
A = [int(x) for x in input().split()]

def F(A, sgn):
  cnt = 0
  cum = 0
  for a in A:
    sgn *= -1
    cum += a
    if cum * sgn > 0:
      continue
    if sgn > 0:
      cnt += 1 - cum
      cum = 1
    else:
      cnt += cum + 1
      cum = -1
  return cnt

answer = min(F(A,1), F(A,-1))
print(answer)