n,k = map(int, input().split())

# 取得される値とその出現回数を保存
d = {}
for _ in range(n):
  a,b = map(int, input().split())
  if a not in d: d[a] = b
  else: d[a] += b

# 値の小さい順にカウントしていき、kを超えた時点の値をk番目の値とする
t = 0
for i in sorted(d.items(), key=lambda x:x[0]):
  t += i[1]
  if t >= k:
    print(i[0])
    exit()