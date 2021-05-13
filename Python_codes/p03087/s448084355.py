N, Q = map(int, input().split())
S = input()
quiz = [list(map(int, input().split())) for _ in range(Q)]

t = [0] * (N+1)
for i in range(N):
  t[i+1] = t[i] + (1 if S[i:i+2] == "AC" else 0)

for q in quiz:
  l = q[0]
  r = q[1]
  print(t[r-1] - t[l-1])