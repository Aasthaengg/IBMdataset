K = int(input())
A = list(map(int, input().split()))

mina = maxa = 2

for a in A[::-1]:
  mina = -(-mina // a) * a
  maxa = maxa // a * a + a - 1
  if mina > maxa:
    print(-1)
    break
else:
  print(mina, maxa)