num = 2000000

n = int(input())
l = list(map(int, input().split()))

max = -num
min = num
total = 0

for x in l:
  if max < x:
    max =x
  if min > x:
    min = x
  total += x

print('%d %d %d'%(min, max, total))
