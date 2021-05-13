N = int(input())
A = list(map(int, input().split()))

def solve(A, mode=0):
  # mode = 0 : +-+-+-...
  # mode = 1 : -+-+-+...
  res = 0
  pre_a = 0
  for i, a in enumerate(A):
    a += pre_a
    if a * (-1)**(i+mode) > 0: # 符号がmatchしている
      pre_a = a
      continue
    # 符号がmatchしていない
    res += abs(a) + 1
    pre_a = (-1) ** (i + mode)
  return res
  
ans = solve(A, mode=0)
ans = min(ans, solve(A, mode=1))
print(ans)