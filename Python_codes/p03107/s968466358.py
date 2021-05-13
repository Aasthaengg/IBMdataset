
def resolve():
    import sys
    input = sys.stdin.readline

    s = input().rstrip()
    r = 0
    b = 0
    for c in s:
        if c == "0":
            r += 1
        else:
            b += 1

    print(min(r, b) * 2)


if __name__ == "__main__":
    resolve()
