N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

D = A - B

L = -1
R = 10 ** 9

while L + 1 < R:
  M = (L + R) // 2
  
  cnt = 0
  for h in H:
    rest = h - M * B
    if rest > 0:
      cnt += - (- rest // D)
  if M >= cnt:
    R = M
  else:
    L = M
print(R)