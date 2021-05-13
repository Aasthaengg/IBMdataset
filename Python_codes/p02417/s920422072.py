import sys
s = sys.stdin.read().lower()

al = [chr(ord("a") + i) for i in range(26)]

for a in al:
  c = 0
  c = s.count(a)
  print('{0} : {1}'.format(a, c))

