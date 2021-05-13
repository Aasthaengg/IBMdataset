N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
F = sorted(list(map(int,input().split())),reverse=True)

l = -1     #スコアが絶対この値より大きくなる数値から始める。
r = 10**13 #スコアが絶対この値より小さくなる数値から始める。
while(l+1<r):
  m = (l+r)//2
  t = 0
  for i in range(N):
    t += max(A[i]-m//F[i],0)
  #print(l,m,r,t)
  if t <= K:
    r = m
  else:
    l = m
print(r)
