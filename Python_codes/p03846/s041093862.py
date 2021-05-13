def abc050_c():
  n = int(input())
  A = list(map(int, input().split()))
  div = 10**9 + 7

  from collections import Counter
  cntr = Counter(A)

  if n % 2 == 0:
    # 偶数個の場合：1,3,5..が2個ずつ
    for i in range(1, n, 2):
      if cntr[i] != 2:
        print(0)
        return
  else:
    # 奇数個の場合：0が1個、2,4,6..が2個ずつ
    if cntr[0] != 1:
      print(0)
      return
    for i in range(2, n, 2):
      if cntr[i] != 2:
        print(0)
        return

  # 半分決まれば残り半分は自動的に決まる
  # nを2で切り捨てた個数 (奇数個のど真ん中は含まない)
  ans = pow(2, n//2, div)
  print(ans)

abc050_c()