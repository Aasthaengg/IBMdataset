N = int(input())
P = tuple(map(int, input().split()))
assert len(P) == N

sortedP = sorted(P)

count = len([p for p,q in zip(P, sortedP) if p != q])
if count == 2 or count == 0:
  print('YES')
else:
  print('NO')