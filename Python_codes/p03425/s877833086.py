n = int(input())

M, A, R, C, H = 0, 0, 0, 0, 0
for i in range(n):
  s = input()
  if s[0] == 'M':
    M += 1
  elif s[0] == 'A':
    A += 1
  elif s[0] == 'R':
    R += 1
  elif s[0] == 'C':
    C += 1
  elif s[0] == 'H':
    H += 1

print(M*A*R + M*A*C + M*A*H + M*R*C + M*R*H + M*C*H + A*R*C + A*R*H + A*C*H + R*C*H)
