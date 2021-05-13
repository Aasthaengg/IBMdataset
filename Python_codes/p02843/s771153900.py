X = int(input())

if X >= 2000:
    print(1)
elif X < 100:
    print(0)
else:
    limit, mods = divmod(X, 100)
    if mods / limit <= 5:
        print(1)
    else:
        print(0)