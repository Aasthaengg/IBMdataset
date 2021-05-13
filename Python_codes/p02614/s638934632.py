H, W, K, = list(map(int, input().split()))
C = [0] * H
for i in range(H):
  C[i] = input()
  C[i] = [1 if(C[i][j] == "#") else 0 for j in range(W)]
h = 2 ** H
w = 2 ** W
ans = 0
cnt = 0
for i in range(2 ** H):
  w = 2 ** W
  for j in range(2 ** W):
    cnt = 0
    for k in range(H):
      for l in range(W):
        if(bin(h)[k + 3] == "0" and bin(w)[l + 3] == "0"):
          cnt += C[k][l]
    ans += (cnt == K)
    w += 1
  h += 1
print(ans)
