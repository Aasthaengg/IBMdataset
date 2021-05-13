def otoshidama(N,Y):
  ansi, ansj, ansk = -1, -1, -1
  if Y/10000 > N:
    return ansi, ansj, ansk
  for i in range(N+1):
    for j in range(N+1-i):
      k = N - i - j
      if i*1000 + j*5000 + k*10000 == Y:
        ansi, ansj, ansk = i, j, k
        return ansi,ansj,ansk
  return ansi,ansj,ansk
N,Y = [int(i) for i in input().split()]
ansi, ansj, ansk = otoshidama(N,Y)
print(ansk, ansj, ansi)