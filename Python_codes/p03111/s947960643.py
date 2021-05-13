from itertools import groupby, accumulate, product, permutations, combinations
def calc(x,X):
  n = len(x)
  if n==0:
    return 10**10
  ans = abs(sum(x)-X)+(n-1)*10
  return ans

def solve():
  ans = 10**10
  N, A, B, C = map(int, input().split())
  L = [int(input()) for _ in range(N)]
  for p in product(['A','B','C','D'],repeat=N):
    a,b,c = [],[],[]
    cnt = 0
    for i in range(N):
      if p[i]=='A':
        a.append(L[i])
      elif p[i]=='B':
        b.append(L[i])
      elif p[i]=='C':
        c.append(L[i])
    cnt += calc(a,A)+calc(b,B)+calc(c,C)
    ans = min(ans,cnt)
  return ans
print(solve())