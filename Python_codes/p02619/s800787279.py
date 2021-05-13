D = int(input())

c = list(map(int,input().split()))

S = []
for i in range(D):
  s = list(map(int,input().split()))
  S.append(s)

T = []
for i in range(D):
  t = int(input())
  T.append(t)

rh = [[0]*26 for i in range(D)]

ans = 0
for i in range(1,D+1):
  m = S[i-1][T[i-1]-1]
  tot = 0
  rh[i-1][T[i-1]-1] += 1 
  for j in range(26):
    last = 0
    for k in range(D):
        if rh[k][j] == 1:
          last = (k+1)
    tot += (c[j]*(i - last))
  ans += m-tot
  print(ans)