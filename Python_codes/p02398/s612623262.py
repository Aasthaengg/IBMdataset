m = map(int, raw_input().split())
c = 0


for i in xrange(m[0],m[1]+1):
  if m[2] % i == 0:
   c = c + 1
print c