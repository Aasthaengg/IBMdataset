n,a,b,c = map(int, input().split())
a,b,c = sorted([a,b,c])
l = [int(input()) for i in range(n)]
ans = 10 ** 18
for i in range(4 ** n):
  LEN = [0,0,0,0]
  num = [0,0,0,0]
  for j,v in enumerate(l):
    index = (i >> (j * 2)) & 3
    LEN[index] += v
    num[index] += 1
  if num[0] and num[1] and num[2]:
    mp = (sum(num[:3])-3) * 10
    d = sorted(LEN[:3])
    mp += abs(d[0]-a) + abs(d[1]-b) + abs(d[2]-c)
    ans = min(ans, mp)
print(ans)