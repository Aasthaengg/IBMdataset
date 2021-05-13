import sys
input = sys.stdin.readline
N = int(input())
print(0)
sys.stdout.flush()
s = input()[: -1]
if s == "Vacant":
  exit(0)
zero = s

ok = 0
ng = N
while ng - ok > 1:
  m = (ok + ng) // 2
  print(m)
  sys.stdout.flush()
  s = input()[: -1]
  if s == "Vacant": exit(0)
  if ((m % 2) and (s != zero)) or ((m % 2 == 0) and (s == zero)): ok = m
  else: ng = m
print(ng)
sys.stdout.flush()
exit(0)