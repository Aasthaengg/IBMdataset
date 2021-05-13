N, M = map(int, input().split())
id = [0 for i in range(N)]

max_l = 0
min_r = 100000
for _ in range(M):
  l, r = map(int, input().split())
  if max_l < l:
    max_l = l
  if min_r > r:
    min_r = r

id = min_r-max_l+1
print(0 if id <0 else id)