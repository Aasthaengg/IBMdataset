import sys
for i in sys.stdin:
    a, b = map(int, i.split())
    p, q = max(a, b), min(a, b)
    while True:
        if p % q == 0:
            break
        else:
            p, q = q, p % q
    print("{} {}".format(q, int(a * b / q)))
