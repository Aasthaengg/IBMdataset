H, W, K = map(int, input().split())
B = [list(input()) for _ in range(H)]
T = 0
for i_1 in range(2**H):
  for i_2 in range(2**W):
    X = [j_1 for j_1 in range(H) if (i_1>>j_1)&1]
    Y = [j_2 for j_2 in range(W) if (i_2>>j_2)&1]
    S = 0
    for x in X:
      for y in Y:
        if B[x][y]=="#":
          S += 1
    if S==K:
      T += 1
print(T)     