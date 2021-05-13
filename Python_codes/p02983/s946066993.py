L, R = [int(n) for n in input().split()]

if R - L >= 2019:
    print(0)
else:
    min_mod = 2019
    for a in range(L, R):
        for b in range(a+1, R+1):
            min_mod = min(min_mod, (a * b) % 2019)

    print(min_mod)