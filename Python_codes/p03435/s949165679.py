def solve():
    import sys
    s = list(map(int, sys.stdin.read().split()))
    x, y, z = s[0] + s[4] + s[8], s[1] + s[5] + s[6], s[2] + s[3] + s[7]
    if x == y == z:
        print("Yes")
    else:
        print("No")


solve()
