def agc026_a():
  n = int(input())
  A = list(map(int, input().split()))
  # 同じ数が連続した個数を2で切り捨て？
  B = []
  num = A[0]
  count = 1
  for i in range(1, n):
    if A[i] == num:
      count += 1
    else:
      B.append(count)
      num = A[i]
      count = 1
  else:
    B.append(count)
  ans = 0
  for b in B:
    ans += b // 2
  print(ans)

agc026_a()