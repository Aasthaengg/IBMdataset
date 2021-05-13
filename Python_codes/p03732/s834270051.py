#ABC060D
N, W = map(int,input().split())
WV = [list(map(int,input().split())) for _ in range(N)]
A = WV[0][0]
B = A + 1
C = A + 2
D = A + 3

AA = []
BB = []
CC = []
DD = []

for wv in WV:
  if wv[0] == A:
    AA.append(wv[1])
  elif wv[0] == B:
    BB.append(wv[1])
  elif wv[0] == C:
    CC.append(wv[1])
  else:
    DD.append(wv[1])

AA = sorted(AA)[::-1]
BB = sorted(BB)[::-1]
CC = sorted(CC)[::-1]
DD = sorted(DD)[::-1]

ans = 0
for a in range(N+1):
  for b in range(N+1-a):
    for c in range(N+1-a-b):
      for d in range(N+1-a-b-c):
        if a > len(AA) or b > len(BB) or c > len(CC) or d > len(DD):
          continue
        if A * a + B * b + C * c + D * d > W:
          continue
        tmp = sum(AA[:a])+sum(BB[:b])+sum(CC[:c])+sum(DD[:d])
        ans = max(ans,tmp)
print(ans)