a,b,c = map(int, input().split())
min_bell = 100000
if a + b < min_bell:
  min_bell = a + b
if a + c < min_bell:
  min_bell = a + c
if c + b < min_bell:
  min_bell = c + b
print(min_bell)