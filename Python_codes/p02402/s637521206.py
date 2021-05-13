import sys

n = int(sys.stdin.readline().strip())
data = sys.stdin.readline().strip().split(' ')

min = None
max = None
sum = 0

for i in range(n):
    num = int(data[i])
    if max is None or num > max:
        max = num

    if min is None or num < min:
        min = num

    sum += num

print('%d %d %d' % (min, max, sum))