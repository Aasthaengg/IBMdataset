n = input()
t, h = 0, 0
for _ in xrange(n):
    taro, hanako = raw_input().split()
    if taro > hanako:
        t += 3
    elif taro == hanako:
        t += 1
        h += 1
    else:
        h += 3
print t, h