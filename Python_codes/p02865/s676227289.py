n = int(raw_input())
if n == 1:
  print 0
  exit(0)
ans = n/2
if n%2 == 0:ans -= 1
print ans
