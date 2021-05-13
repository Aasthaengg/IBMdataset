from itertools import groupby, accumulate, product, permutations, combinations
def calc(x,X):
  n = len(x)
  ans = 10**10
  for q in product([0,1],repeat=n):
    point = 0
    cnt = 0
    for i in range(n):
      if q[i]==1:
        if cnt>0:
          point += 10
        cnt += x[i]
    if cnt>0:
      point += abs(cnt-X)
    else:
      point = 10**10
    ans = min(point,ans)
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