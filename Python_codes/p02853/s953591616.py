from collections import defaultdict
X, Y = map(int, input().split())
d = defaultdict(int)
d[1] = 300000
d[2] = 200000
d[3] = 100000
ans = d[X]+d[Y]
if X==1 and Y==1:
  ans += 400000
print(ans)