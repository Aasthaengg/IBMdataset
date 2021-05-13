n, h, w = map(int, raw_input().split())

count = 0
for i in xrange(n):
    a, b = map(int, raw_input().split())

    if a >= h and b >= w:
        count += 1

print count