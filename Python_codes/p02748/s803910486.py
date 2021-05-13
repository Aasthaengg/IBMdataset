import sys
# input = sys.stdin.readline

def readlines(n):
    for _ in range(n):
        x, y, c = map(int, input().split())
        yield x-1, y-1, c

def main():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    yield(min(a) + min(b))

    for x, y, c in readlines(M):
        a_ = a[x]
        b_ = b[y]

        yield a_ + b_ - c

print(min(main()))
