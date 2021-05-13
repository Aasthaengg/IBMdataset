N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dif = [A[i] - B[i] for i in range(N)]
if sum(A) < sum(B):
  print(-1)
else:
  dif.sort()
  if dif[0] >= 0:
    print(0)
  else:
    p, n = N - 1, 0
    while dif[n] < 0:
      n += 1
    ms = sum(-dif[i] for i in range(n))
    S = dif[p]
    num = n + 1
    while S < ms:
      p -= 1
      S += dif[p]
      num += 1
    print(num)