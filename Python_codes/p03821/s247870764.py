n = int(input())
abl = [list(map(int,input().split())) for nesya in range(n)]
c = 0
abl = abl[::-1]
for ab in abl:
  a = ab[0] + c
  b = ab[1]
  if a%b == 0:
    continue
  c += (b - a%b)
print(c)
