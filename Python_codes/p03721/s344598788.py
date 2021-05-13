n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
#print(ab)
ab.sort()
#print(ab)
for i in range(n):
  k = k-ab[i][1]
  if k <= 0:
    print(ab[i][0])
    exit()