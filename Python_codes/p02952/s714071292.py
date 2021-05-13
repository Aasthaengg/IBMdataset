import sys


def rec(length):
    if length == 1:
        return 9
    else:
        return 9 * 10**(length - 1) + rec(length - 2)


n = input()
length = len(n)

if length == 1:
    print(n)
    sys.exit()

if length % 2 == 0:
    ans = rec(length - 1)
else:
    ans = rec(length - 2) + int(n) - int("1" + "0" * (length - 1)) + 1

print(ans)