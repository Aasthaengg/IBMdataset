m, k = map(int, input().split())
limit = 2 ** m

if k >= limit:
  print(-1)
  exit()

if m == 0:
  print(0, 0)
elif m == 1:
  if k == 0:
    print(0, 0, 1, 1)
  elif k == 1:
    print(-1)
else:
  A = [i for i in range(limit) if i != k]
  ans = A + [k] + A[::-1] + [k]
  print(' '.join(map(str, ans)))