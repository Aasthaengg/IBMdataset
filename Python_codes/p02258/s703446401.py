n = int( raw_input() )

min = 10 ** 10
ans = -10 ** 10


for i in xrange(n):
  x = int( raw_input() )
  if x - min > ans:
    ans = x - min
  if x < min:
    min = x

print ans