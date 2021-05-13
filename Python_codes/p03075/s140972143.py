def solve():
    import sys
    read = sys.stdin.read
    *s, k = map(int, read().split())
    flg = True
    for a in s:
        for b in s:
            if abs(a - b) > k:
                flg = False
    print("Yay!" if flg else":(")

solve()