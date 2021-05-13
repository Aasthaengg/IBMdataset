n = int(input())
a = input()
b = input()
c = input()

ans = 0
for i in range(n):
  if a[i] == b[i] and b[i] == c[i]:
    # すべて同じなので操作しなくて良い
    continue

  if a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
    # すべて異なるので操作2回
    ans = ans + 2
    continue

  # 1つ異なる
  ans = ans + 1

print(ans)