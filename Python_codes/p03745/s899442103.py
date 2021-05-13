def check(a,b):
  if a<b:
    return 'up'
  if a>b:
    return 'down'
  return ''

def solve():
  ans = 1
  N = int(input())
  A = list(map(int, input().split()))
  ud = ''
  for i in range(N-1):
    a = check(A[i],A[i+1])
    if ud=='' or ud==a:
      ud = a
      continue
    if a=='':
      continue
    ans += 1
    ud = ''
  return ans
print(solve())
