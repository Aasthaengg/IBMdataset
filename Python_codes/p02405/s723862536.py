import sys


h, w = map(int, input().split())
while h != 0:
    a = "#"
    b = "."
    for _ in range(h):
        for i in range(w):
            if i % 2 == 0:
                sys.stdout.write(a)
            else:
                sys.stdout.write(b)
        a, b = b, a
        print()
    print()
    h, w = map(int, input().split())

