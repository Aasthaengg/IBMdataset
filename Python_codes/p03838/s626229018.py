x, y = map(int, input().split());

MAX = 100000000000000;

# どれが最小かを考える
# そのまま近づける
a = y - x;
if (a < 0):
  a = MAX;
# xを反転させて近づける
b = y + x;
if (b < 0):
  b = MAX;
# yを反転
c = y * (-1) - x;
if (c < 0):
  c = MAX;
# xとyの両方を反転させて近づける
d = y * (-1) + x;
if (d < 0):
  d = MAX;

# 最小を求める
ans = min(a, b + 1, c + 1, d + 2);
print(ans);