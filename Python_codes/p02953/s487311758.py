N = int(input())
H = tuple(reversed(tuple(map(int, input().split()))))
assert len(H) == N

result = True
prev = None
for i,h in enumerate(H):
  if prev is not None:
    if h > prev + 1:
      result = False
      break
    if h < prev + 1:
      prev = h
  else:
    prev = h
print('Yes' if result else 'No')