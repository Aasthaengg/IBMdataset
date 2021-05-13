n = int(input())
l = list(map(int, input().split()))

while len(l) > 1:
  l = sorted(l)
  f = l.pop(0)
  s = l.pop(0)
  l.append( ( f + s ) / 2 )

print(l[0])