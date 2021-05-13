N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

def f(s1, s2):
  a = s1[0]
  b = s1[1]
  c = s2[0]
  d = s2[1]
  if a>c:
    a,b,c,d = c,d,a,b
  if b<c:
    return [-1, -1]
  return [c, min(b,d)]

Mlist_T = [[1, 1] for i in range(N)]#第一要素は最小値、第二要素は最大値のリスト
Mlist_A = [[1, 1] for i in range(N)]
Mlist_T[0][0]=T[0]
Mlist_T[0][1]=T[0]
Mlist_A[N-1][0]=A[N-1]
Mlist_A[N-1][1]=A[N-1]
for i in range(1,N):
  if T[i-1] != T[i]:
    Mlist_T[i][0] = T[i]
  Mlist_T[i][1] = T[i]
for i in range(1,N):
  if A[N-1-(i-1)] != A[N-1-i]:
    Mlist_A[N-1-i][0] = A[N-1-i]
  Mlist_A[N-1-i][1] = A[N-1-i]
fl = True
M = []
for i in range(N):
  m = f(Mlist_T[i],Mlist_A[i])
  if m == [-1, -1]:
    fl = False
    print(0)
    break
  M.append(m)

if fl:

  r = 1000000007
  ss = 1

  for m in M:
    ss = (ss * (m[1]-m[0]+1))%r
  print(ss)