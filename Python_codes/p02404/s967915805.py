import sys


h, w = map(int, input().split())
while h != 0:
    print("#"*w)
    for _ in range(h-2):
        for i in range(w):
            if i == 0 or i == w-1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print()
    print("#" * w)
    print()
    h, w = map(int, input().split())

