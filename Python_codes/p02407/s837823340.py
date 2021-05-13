import sys
n = input()
a = map(int, raw_input().split())
for i in range(n):
  sys.stdout.write('%d' % a[n-i-1])
  if i != n-1:
    sys.stdout.write(' ')
sys.stdout.write('\n')