n, t = map(int, input().split())
# 経路の最小コスト
a = 10**19
for _ in range(n):
    c, tt = map(int, input().split())
    if t >= tt:
        a = min(c, a)
# 対象経路がない
if a == 10**19:
    print('TLE')
else:
    print(a)
