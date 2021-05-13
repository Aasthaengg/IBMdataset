import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    s = int(input().rstrip())
    opened = set()
    opened.add(s)
    prev = s
    m = 1
    while True:
        m += 1
        y = int(prev / 2) if prev % 2 == 0 else (3 * prev + 1)
        if y in opened:
            print(m)
            break
        prev = y
        opened.add(y)









if __name__ == "__main__":
    resolve()
