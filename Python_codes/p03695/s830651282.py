N = int(input())
A = list(map(int, input().split()))

cnt = [False] * 8
free = 0

for a in A:
  c = a // 400
  if c >= 8:
    free += 1
  else:
    cnt[c] = True

max_c = sum(cnt) + free
if sum(cnt) != 0:
  min_c = sum(cnt)
else:
  min_c = 1

print(min_c, max_c)
