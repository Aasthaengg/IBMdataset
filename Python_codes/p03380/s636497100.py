n = int(input())
a = list(map(int, input().split()))
m = max(a)
r = -1
for i in a:
  if i != m and abs(m - 2 * i) < abs(m - 2 * r):
    r = i
print(m, r)
