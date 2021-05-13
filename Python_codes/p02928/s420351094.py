def resolve():
  mod = 1000000007
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  x = 0
  # A の転倒数を求める
  for i in range(n):
    for j in range(i+1, n):
      if a[i] > a[j]:
        x += 1
  # A のすべての数字に対して，A内に自分より小さいものが何個あるか
  y = 0
  for i in range(n):
    for j in range(n):
      if a[i] > a[j]:
        y += 1
  ans = (x * k) % mod
  # 1 ~ k の和 * y
  ans += (((k-1) * (k)) // 2) * y % mod
  ans %= mod

  print(ans)
  return

if __name__ == "__main__":
  resolve()
