A, B, C = map(int, input().split())

if A == B and B == C:
  if A % 2 == 0:
    print(-1)
    exit(0)
  else:
    print(0)
    exit(0)

cnt = 0
for _ in range(1000):
  if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
    print(cnt)
    exit(0)
  tA, tB, tC = A, B, C
  A = (tB + tC) // 2
  B = (tA + tC) // 2
  C = (tA + tB) // 2
  cnt += 1
