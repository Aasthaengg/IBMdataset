N = int(input())
S = list(input())
W = 0
E = S[1:].count('E')
Turn = []
Turn.append(E)

for i in range(1, N):
  if S[i] == 'E':
    E -= 1
  if S[i-1] == 'W':
    W += 1
  Turn.append(E+W)

print(min(Turn))