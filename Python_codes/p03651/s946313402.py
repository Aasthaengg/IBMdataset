from fractions import gcd
def agc018_a():
  n, k = map(int, input().split())
  A = list(map(int, input().split()))
  A = sorted(A)
  # 元の数列の最大を超える数は作れない
  if A[-1] < k:
    print('IMPOSSIBLE')
    return
  # 数列要素のgcdを求める
  g = A[0]
  for a in A:
    g = gcd(g, a)
    # 元の数列内に存在していれば即OK
    if a == k:
      print('POSSIBLE')
      return
  # gcdで割れる値なら作り出せる？？
  if k % g == 0:
    print('POSSIBLE')
  else:
    print('IMPOSSIBLE')

agc018_a()