import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

x, n = inm()
a = inl()
count = 1
if x not in a:
    print(x)
else:
    while True:
        if x - count not in a:
            print(x - count)
            break
        if x + count not in a:
            print(x + count)
            break
        count += 1