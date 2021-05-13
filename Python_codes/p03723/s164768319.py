A, B, C = map(int, input().split())
res = 0

if (A == B == C) and all([A % 2 ==0, B % 2 == 0, C % 2 ==0]):
  res = -1
else:
  while all([A % 2 ==0, B % 2 == 0, C % 2 ==0]):
    at, bt, ct = A/2, B/2, C/2
    A = bt + ct
    B = at + ct
    C = at + bt
    res += 1

print(res)