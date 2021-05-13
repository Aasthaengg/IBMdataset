"""
i - j = A[i] + A[j]
> i - A[i] = j + A[j]
i > j
"""
N = int(input())
high = list(map(int, input().split()))

ans = 0
calc = {}
for i in range(1, N+1):
  try:
    ans += calc[i - high[i-1]]
  except KeyError:
    pass
  if (i + high[i-1]) in calc.keys():
    calc[i + high[i-1]] += 1
  else:
    calc[i + high[i-1]] = 1

print(ans)