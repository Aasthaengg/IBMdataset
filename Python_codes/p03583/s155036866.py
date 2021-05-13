N = int(input())
if N % 4 == 0:
  h, n, w = (3 * N) // 4, (3 * N) // 4, (3 * N) // 4
elif N % 4 == 2:
  h, n, w = N, N, N // 2
elif N % 4 == 3:
  s = N // 4 + 1
  h, n, w = 2 * s, 2 * s, s * N
elif N % 4 == 1:
  s = (N // 4) + 1
  if s % 3 == 0:
    h = s
    n = 2 * (s // 3) * (4 * s - 3)
    w = 2 * (s // 3) * (4 * s - 3)
  elif s % 3 == 2:
    h = N
    n = 4 * (s // 3) + 2
    w = (4 * (s // 3) + 2) * (12 * (s // 3) + 5)
  elif s % 3 == 1:
    l = (N+3)//4
    p = 0
    for i in range(l, 3501):
      m = (N*i)//(4*i-N)+1
      for j in range(m, 3501):
        #print(i, j, (N*i*j)%(4*i*j-N*(i+j)), 4*i*j-N*(i+j))
        if (N*i*j) % (4*i*j-N*(i+j)) == 0 and 4*i*j-N*(i+j) > 0:
          p = 1
          h, n, w = i, j, (N*i*j) // (4*i*j-N*(i+j))
          break
      if p == 1:
        break
print(h, n, w)