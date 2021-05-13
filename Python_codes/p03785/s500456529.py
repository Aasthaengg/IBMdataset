n, c, k = map(int, input().split())
T = sorted(int(input()) for _ in range(n))

counter = 1
start = -1
wating_num = 0
for t in T:
  if start < 0:
    start = t
  if t - start > k or wating_num + 1 > c:
    counter += 1
    wating_num = 0
    start = t
  wating_num += 1
print(counter)