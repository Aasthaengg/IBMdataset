n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]

dsum = 0

for i in range(n-1):
  for j in range(i+1, n):
    d = ( (xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2 )**0.5
    dsum += d

dave = dsum / (n*(n-1) / 2)

print(dave*(n-1))