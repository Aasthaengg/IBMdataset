from sys import stdin
a = stdin.readline().strip()
n  = int(stdin.readline())
ans = ''
m = len(a)
for  i in xrange(m):
 if i%n==0:
  ans += a[i]
print ans