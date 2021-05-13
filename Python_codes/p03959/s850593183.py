N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
INF = 10**10
MOD = 10**9 + 7

H = [0] * N
_H = [INF] * N
pre_h = 0
for i, h in enumerate(T):
  if h != pre_h:
    H[i] = h
    pre_h = h
  else:
    _H[i] = min(_H[i], h)

pre_h = 0
for i, h in enumerate(A[::-1], 1):
  if h != pre_h:
    if (H[-i] > 0 and H[-i] != h) or _H[-i] < h:
      print(0)
      quit()
    H[-i] = h
    pre_h = h
  else:
    _H[-i] = min(_H[-i], h)

ans = 1
for h, _h in zip(H, _H):
  if h == 0:
    ans *= _h
    ans %= MOD

print(ans)