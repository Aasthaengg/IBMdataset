n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
y = 0
for i in range(2 ** n):
  v_total = 0
  c_total = 0
  for j in range(n):  # このループが一番のポイント
    if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
      v_total += v[j]
      c_total += c[j]
  if (v_total-c_total) > y:
    y = v_total-c_total
print(y)