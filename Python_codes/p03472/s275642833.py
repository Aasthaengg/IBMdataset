N, H = map(int, input().split())

a = [0] * N
b = [0] * N

ab = []
for i in range(N):
  ai, bi = map(int, input().split())
  a[i] = -ai
  b[i] = -bi
  ab.append((-ai, -bi))
  
ab.sort()
b.sort()
mina = ab[0][0]

ans = 0
for bi in b:
  if bi <= mina:
    H += bi
    ans += 1
    if H <= 0:
      print(ans)
      exit()
  else:
    ans += (H-1)//(-mina) + 1
    print(ans)
    exit()
ans += (H-1)//(-mina) + 1
print(ans)
