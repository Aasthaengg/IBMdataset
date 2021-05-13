def prime_factorize(n):
  # nの素因数分解
  a = []
  while n % 2 == 0:
    a.append(2)
    n = n // 2
  f = 3
  while f * f <= n:
    if n % f == 0:
      a.append(f)
      n = n // f
    else:
      f += 2
  if n != 1:
    a.append(n)
  return a

def abc052_c():
  n = int(input())
  if n == 1:
    print(1)
    return

  # 2...nを素因数分解してすべて集める
  primes = []
  for i in range(2, n+1):
    primes += prime_factorize(i)

  # N!の約数を生成する組合せ数
  # 各素因数の出現回数+1(何も使わないも含めて)を掛け合わせる
  div = 10**9 + 7
  ans = 1
  from collections import Counter
  for kv in Counter(primes).items():
    ans = ans * (kv[1] + 1) % div
  print(ans)

abc052_c()