nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

a, b, c = nl()
if b - a == c - b:
    print('YES')
else:
    print('NO')
