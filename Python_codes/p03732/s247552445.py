N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 10
w0 = INF
for w, v in wv:
  w0 = min(w0, w)

for i in range(N):
  wv[i][0] -= w0
#print("wv:", wv)

U = [[] for _ in range(4)]
for w, v in wv:
  U[w].append(v)
  
for i in range(4):
  U[i].sort(reverse = True)
#print("U:", U)

S = [[0] for _ in range(4)]
for i in range(4):
  for u in U[i]:
    S[i].append(S[i][-1] + u)
#print("S", S)

answer = []
for i0 in range(len(S[0])):
  for i1 in range(len(S[1])):
    for i2 in range(len(S[2])):
      for i3 in range(len(S[3])):
        if i1 + i2 * 2 + i3 * 3 + (i0 + i1 + i2 + i3) * w0 <= W:
          answer.append(S[0][i0] + S[1][i1] + S[2][i2] + S[3][i3])
print(max(answer))