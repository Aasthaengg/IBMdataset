a, b, c = map(int, input().split())

cnt = 0

if a >= b+c:
    print(0)
elif c - (a-b) <= 0:
    print(0)
else:
    print(c - (a-b))