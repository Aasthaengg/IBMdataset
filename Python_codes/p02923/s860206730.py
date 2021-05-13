N = int(input())
H = [int(x) for x in input().split()]

if N == 1:
  print(0)
else:
  ans = []
  c = 0
  for i in range(N - 1):
    if H[i] >= H[i + 1]:
      c += 1
      if i == N - 2:
        ans.append(c)
    elif H[i] < H[i + 1]:
      ans.append(c)
      c = 0
  print(max(ans))