import math
mod = 10 ** 9 + 7
def combinations_count(n, r): # 組み合わせ
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())

if N < 3:
  print(0)
elif N == 3:
  print(1)
else:
  ans = 0
  num_digit = N // 3 # 項数を計算する
  for i in range(num_digit): # 可能な項数ごとに計算する 1 <= x <= num_digit, 仕切りの数は0 <= x < num_digit
    combi = combinations_count((N - (3 * (i+1)) + i), i) # 数字と項数区切りの組み合わせを計算する ex. oo|
    ans += combi
  if ans >= mod:
    print(int(ans % mod))
  else:
    print(ans)