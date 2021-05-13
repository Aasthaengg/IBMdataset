import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(read())
for i in range(1, 3500):
    for h in range(1, 3500):
        check = 4 * i * h - n * (i + h)
        if check > 0:
            v = n * i * h / check
            if v.is_integer():
                print(i, h, int(v))
                exit()
