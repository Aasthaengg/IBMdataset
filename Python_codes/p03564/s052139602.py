N = int(input())
K = int(input())
cur = 1

while N > 0:
  tmp1 = cur + K
  tmp2 = cur * 2
  cur = min(tmp1, tmp2)
  N -= 1

print(cur)