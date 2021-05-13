import sys
readline = sys.stdin.readline

# そこまでの最小値を記録する
# 最小値との差が最大になった時点で、その値を記録し、1を計上
# 最小値との差がこれまでの最大値と同じ場合は+1を計上
# 最小値との差の最大値が更新された場合はまた1から計上
# Tは関係ない

N,T = map(int,readline().split())
A = list(map(int,readline().split()))

minval = 10 ** 9 + 1 # そこまでの最小値
maxdiff = 0 # そこまでの差の最大値
ans = 0
for a in A:
  if a < minval:
    minval = a
    continue
  diff = a - minval
  if diff > maxdiff:
    maxdiff = diff
    ans = 1
  elif diff == maxdiff:
    ans += 1

print(ans)