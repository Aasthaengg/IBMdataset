n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab = ab[::-1]

z = 0
cnt = 0
for a, b in ab:
  a += z
  if a % b != 0:
    z += b - (a % b)
print(z)
