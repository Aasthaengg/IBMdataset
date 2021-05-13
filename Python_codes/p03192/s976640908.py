n = int(raw_input())

count = 0

for i in xrange(4):

    if (n % 10) == 2:
        count += 1

    n /= 10

print count