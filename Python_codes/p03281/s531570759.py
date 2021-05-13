N = int(input())

def divisor_pairs(n):
  # n の正の約数の数
  # ペアの数を保存しておけばいい
  pairs = 0

  # 約数判定はO(√N)で出来るということを知っておく
  i = 1

  while i * i <= n:
    if n % i == 0:
      pairs += 1
    i += 1
  return pairs

result = 0

# 奇数なのでステップ数を2に指定
for x in range(1, N+1, 2):
  if divisor_pairs(x) == 4:
    result += 1

print(result)