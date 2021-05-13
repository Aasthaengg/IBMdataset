import copy

H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]
k = sum([ci.count("#") for ci in c])
ans = 0

for i2 in range(2 ** H):
  for j2 in range(2 ** W):
    cr = copy.deepcopy(c)
    for k in range(H+1):
      if i2 & 2**k == 2**k:
        for j in range(W):
          cr[k][j] = "$"
    for l in range(W+1):
      if j2 & 2**l == 2**l:
        for i in range(H):
          cr[i][l] = "$"
    if K == sum([ci.count("#") for ci in cr]):
      ans += 1
    
print(ans)