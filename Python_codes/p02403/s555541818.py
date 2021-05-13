import sys
h, w = map(int, input().split())
while h != 0:
    for _ in range(h):
        for _ in range(w):
            sys.stdout.write("#")
        print()
    print()
    h, w = map(int, input().split())
