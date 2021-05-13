from itertools import permutations
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
t = 0
for i in permutations(xy, n):
  t += 1
  for j in range(n-1):
    ans += ((i[j][0] - i[j+1][0])**2 + (i[j][1] - i[j+1][1])**2)**0.5
print(ans/t)