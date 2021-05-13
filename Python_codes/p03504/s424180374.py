N, C = map(int, input().split())
stc = [list(map(int, input().split())) for _ in range(N)]

max_t = 0
for s, t, c in stc:
  max_t = max(max_t, t)

T = [[0 for _ in range(max_t + 2)] for _ in range(C + 1)] 
for i in range(N):
  s, t, c = stc[i]
  T[c][s] = t - s + 1
#print("T:", T[1:])

for c in range(1, C + 1):
  for i in range((max_t + 2) - 1):
    if T[c][i]:
      if T[c][i + 1] == 0:
        T[c][i + 1] = T[c][i] - 1
      T[c][i] = 1      
#print("T:", T[1:])

answer = []
for i in range(max_t + 2):
  cnt = 0
  for c in range(1, C + 1):
    if T[c][i]:
      cnt += 1
  answer.append(cnt)
#print("answer:", answer)
print(max(answer))