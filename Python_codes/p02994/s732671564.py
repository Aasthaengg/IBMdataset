n, l = map(int, input().split())
expected = sum([l+i-1 for i in range(1, n+1)])

diff = 10 ** 9
result = 10 ** 9

for i in range(1, n+1):
  reduced = expected - (l+i-1)
  if abs(expected - reduced) < diff:
    diff = abs(expected - reduced)
    result = reduced

print(result)