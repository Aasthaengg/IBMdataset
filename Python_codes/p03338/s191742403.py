N = int(input())
S = input()
answer = 0
for i in range(1,N-1):
  X = S[:i]
  Y = S[i:]
  Z = 0
  for c in 'abcdefghijklmnopqrstuvwxyz':
    if c in X and c in Y:
      Z += 1
  answer = max(answer,Z)
print(answer)