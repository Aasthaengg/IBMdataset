import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int, read().split()))

dic = {}
ans = 0

for i in range(n):
  ans += 1
  try:
    dic[a[i]] += 1
    if dic[a[i]] == a[i]:
      ans -= a[i]
  except KeyError:
    dic[a[i]] = 1
    if dic[a[i]] == a[i]:
      ans -= a[i]

print(ans)
