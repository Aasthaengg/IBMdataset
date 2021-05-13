n = input()
sum = 0
a = map(int, raw_input().split())
a.sort()
for i in range(n):
  sum += a[i]
print '%d %d %d' % (a[0], a[n-1], sum)