A, B, C, D, E, F = map(int, input().split())
perc = 0.0
ans = [0, 0]
op = [0, 0, 0, 0]
a = 0
while 100 * a <= F:
  b = 0
  while 100 * (a + b) <= F:
    c = 0
    while 100 * (a + b) + c <= F:
      if c > (a + b) * E:
        break
      d = 0
      while 100 * (a + b) + c + d <= F:
        if c + d > (a + b) * E:
          break
        if a == b == c == d == 0:
          break
        p = (c + d) * 1.0 / (100 * (a + b) + c + d)
        if p >= perc:
          perc = p
          ans = [100 * (a + b) + c + d, c + d]
          op = [a, b, c, d]
        d += D
      c += C
    b += B
  a += A
print(str(ans[0]) + " " + str(ans[1]))