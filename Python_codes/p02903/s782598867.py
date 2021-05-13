def slove():
    import sys
    input = sys.stdin.readline
    h, w, a, b = list(map(int, input().rstrip('\n').split()))
    for i in range(h):
        if i < b:
            t = ["0"] * a
            s = ["1"] * (w - a)
            print("".join(t + s))
        else:
            t = ["1"] * a
            s = ["0"] * (w - a)
            print("".join(t + s))


if __name__ == '__main__':
    slove()
