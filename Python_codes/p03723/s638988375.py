import sys
a, b, c = [int(w) for w in input().split()]

ans = 0


def is_fin(a, b, c):
    global ans
    if a % 2 or b % 2 or c % 2:
        return True
    elif a == b == c:
        ans = -1
        return True
    else:
        return False


while not is_fin(a, b, c):
    ta = (b+c)/2
    tb = (a+c)/2
    tc = (a + b) / 2
    a, b, c = ta, tb, tc
    ans += 1

print(ans)
