W, a, b = map(int, input().split())
sub = abs(a - b)

if sub - W > 0:
    print(sub - W)
else:
    print(0)
