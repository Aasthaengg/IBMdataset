n = int(input())
s = [input() for _ in range(2)]
mod = 10 ** 9 + 7


def is_vertical(i):
    return s[0][i] == s[1][i]


i = 0
if is_vertical(i):
    ans = 3
    prev_is_vertical = True
    i += 1
else:
    ans = 3 * 2
    prev_is_vertical = False
    i += 2

while i < n:
    if is_vertical(i):
        if prev_is_vertical:
            ans *= 2
        else:
            ans *= 1
        prev_is_vertical = True
        i += 1

    else:
        if prev_is_vertical:
            ans *= 2
        else:
            ans *= 3
        prev_is_vertical = False
        i += 2

    ans %= mod

print(ans)
