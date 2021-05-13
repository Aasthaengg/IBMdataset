import bisect
INF = 10**15
A, B, Q = map(int, input().split())
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]
for i in range(Q):
  x = int(input())
  sw = bisect.bisect_right(s, x)-1 #xより西で一番近い(同じ場所でもいい)神社の番号
  se = sw + 1 #xより東で一番近い神社の番号
  tw = bisect.bisect_right(t, x)-1
  te = tw + 1
  res = INF
  for S in [s[sw], s[se]]:
    for T in [t[tw], t[te]]:
      d1, d2 = abs(x-S) + abs(T-S), abs(x-T) + abs(S-T)
      res = min(res, d1, d2)
  print(res)

