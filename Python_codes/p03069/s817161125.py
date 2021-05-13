import itertools

N = int(input())
S = input()

black = [0] * (N + 1)
white = [0] * (N + 1)
for i, s in enumerate(S, 1):
  if s == '#':
    black[i] += 1
  else:
    white[i] += 1

black = list(itertools.accumulate(black))
white = list(itertools.accumulate(white))

ans = N
num_W = white[-1]
for b, w in zip(black, white):
  ans = min(ans, b + (num_W-w))

print(ans)