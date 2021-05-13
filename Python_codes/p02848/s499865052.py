alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = int(input())
S = list(input())
for i in S:
  idx = alpha.index(i)
  n_idx = (idx + N) % 26
  print(alpha[n_idx],end="")