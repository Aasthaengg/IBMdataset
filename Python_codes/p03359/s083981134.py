nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

a, b = nl()

if a <= b:
    print(a)
else:
    print(a-1)
