H, W = map(int, input().split())
l = []
for _ in range(H):
  l.append(list(input()))

for row in l:
  for _ in range(2):
	  print(''.join(row))