N, Y = [int(s) for s in input().split(" ")]
Y = int(Y/1000)
# 10a + 5b + c = Y
# a + b + c = N
ans = []
for i in range(N + 1):
  for j in range(N + 1 - i):
    if N - i - j >= 0 and Y - 10 * i - 5 * j == N - i - j:
      ans += [str(i), str(j), str(N - i - j)]
      break
  else:
    continue
  break


if len(ans):
  print(" ".join(ans))
else:
  print("-1 -1 -1")