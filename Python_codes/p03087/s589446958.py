N, Q = map(int, input().split())
S = input()
L = [list(map(int, input().split())) for _ in range(Q)]
t, I = 0, [0]
for i in range(1, N):
  if S[i-1]=="A":
    if S[i]=="C":
      t += 1
  I.append(t)
for l in L:
  print(I[l[1]-1]-I[l[0]-1])