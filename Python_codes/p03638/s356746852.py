H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ans = [[0] * W for h in range(H)]
h = 0
w = 0
t = 0

for index, a in enumerate(A):
  for i in range(a):
    ans[h][w] = index+1

    if t == 0 and w+1 < W:
      w += 1
      continue

    if t == 0 and w+1 >= W:
      h += 1
      t = 1
      continue

    if t == 1 and w-1 >= 0:
      w -= 1
      continue

    if t == 1 and w-1 < 0:
      h += 1
      t = 0
      continue

for i in ans:
  for k in i:
    print(k, end=" ")

  print("")