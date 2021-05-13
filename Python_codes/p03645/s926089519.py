n,m = map(int, input().split())
set_a = set()
set_b = set()
AB = [list(int(x) for x in input().split()) for _ in range(m)]


for a,b in AB:
  if a > b:
    a,b = b,a
  
  if a == 1:
    set_a.add(b)
  if b == n:
    set_b.add(a)

se = set_a & set_b
print('POSSIBLE' if se else 'IMPOSSIBLE')