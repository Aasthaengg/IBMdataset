import sys
count = 1
while True:
    x = sys.stdin.readline().strip()
    if x == '0':
        break
    print("Case %d: %s" % (count, x))
    count += 1