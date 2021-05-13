X, Y = [int(n) for n in input().split(sep=' ')]
print(X if X % Y != 0 else -1)