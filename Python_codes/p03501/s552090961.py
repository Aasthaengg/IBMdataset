N, A, B = map(int, input().split())

if N*A >= B:
  r = B
else:
  r = N*A
print(int(r))