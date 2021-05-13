n = int(raw_input())
a = map(int, raw_input().split(" "))

min = 1000000
max = -1000000
sum = 0
for x in a:
  if x < min:
    min = x
  if x > max:
    max = x
  sum += x

print "%d %d %d" % (min, max, sum)