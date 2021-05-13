import sys
A, B, C = list(map(int, input().split()))

cnt = 0
while A%2 == 0 and B%2 == 0 and C%2 == 0:
  tmp1 = B/2 + C/2
  tmp2 = C/2 + A/2
  tmp3 = A/2 + B/2
  A = tmp1
  B = tmp2
  C = tmp3
  cnt += 1
  if cnt >= 10**4:
    print("-1")
    sys.exit()
print(cnt)