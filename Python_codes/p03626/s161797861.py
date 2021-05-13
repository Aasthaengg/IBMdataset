n = int(input())
S1 = input()
S2 = input()
mod = 10**9 + 7

prev = 0  # 0 = first, 1 = vertical, 2 = horizontal

pattern = 1
skip = False
for s1, s2 in zip(S1, S2):
    if skip:
        skip = False
        continue

    if s1 == s2:
        block = 1
    else:
        block = 2
        skip = True

    if prev == 0:
        if block == 1:
            pattern = pattern * 3 % mod
            prev = 1
        else:
            pattern = pattern * 6 % mod
            prev = 2

    elif prev == 1:
        if block == 1:
            pattern = pattern * 2 % mod
            prev = 1
        else:
            pattern = pattern * 2 % mod
            prev = 2

    elif prev == 2:
        if block == 1:
            prev = 1
        else:
            pattern = pattern * 3 % mod
            prev = 2

print(pattern)
