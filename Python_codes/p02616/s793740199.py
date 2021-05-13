n, k = map(int, input().split())
a = [int(i) for i in input().split()]
MOD = 10 ** 9 + 7
s, t = [], []  # 正、負の配列
for i in a:
  if i < 0:
    t.append(i)
  else:
    s.append(i)
S, T = len(s), len(t)
is_positive = False  # 積が正である
if S > 0:
  # 正の数が0より大きい
  if n == k:
    # nとkが同じ
    is_positive = (T % 2 == 0) # 負の数が偶数個のとき、積は正
  else:
    is_positive = True
else:
  is_positive = (k % 2 == 0)

ans = 1
if not is_positive:
  a.sort(key=abs)
  for i in range(k):
    ans = ans * a[i] % MOD
else:
  s.sort()
  t.sort(reverse=True)
  if k % 2 == 1:
    ans = ans * s.pop(-1) % MOD
  p = []
  while(len(s) >= 2):
    x = s.pop(-1)
    x *= s.pop(-1)
    p.append(x)
  while(len(t) >= 2):
    x = t.pop(-1)
    x *= t.pop(-1)
    p.append(x)
  p.sort(reverse=True)
  for i in range(k // 2):
    ans = ans * p[i] % MOD
print(ans)