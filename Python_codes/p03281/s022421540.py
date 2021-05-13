# 引数nが持つ正の約数の数を調べる
def divisor_count(n:int) -> int:
  count = 0
  for x in range(1, n+1):
    if n % x == 0:
      count += 1
  
  return count

def solve(n: int) -> int:
  # [1..N]内で奇数かつ約数をちょうど8個持つ数字の数
  result = 0
  for x in range(1, n+1, 2):
    if divisor_count(x) == 8:
      result += 1
  return result
  
N = int(input())
print(solve(N))