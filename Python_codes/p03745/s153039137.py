n = int(input())
a = list(map(int, input().split()))

cnt = 1
mono = 0
for i in range(1, n):
  d = a[i] - a[i - 1]
  if d * mono < 0:
    cnt += 1
    mono = 0
  elif d != 0:
    mono = d
print(cnt)