N, L = list(map(lambda x: int(x), input().split(" ")))
 
S = int(N * (N-1) / 2) + L * N
 
if L >= 0:
  print(S - L)
elif L + N - 1 <= 0:
  print(S - L - N + 1)
else:
  print(S)