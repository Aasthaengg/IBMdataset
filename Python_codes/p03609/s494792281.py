X, t = map(int, input().split(" "))

rest = X - t

if rest < 0:
    print(0)
else:
    print(rest)
