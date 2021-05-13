import sys
def input(): return sys.stdin.readline().strip()


def main():
    sx, sy, tx, ty = map(int, input().split())
    dx, dy = tx - sx, ty - sy
    ans = ""
    for _ in range(dx): ans += "R"
    for _ in range(dy): ans += "U"
    for _ in range(dx): ans += "L"
    for _ in range(dy): ans += "D"
    ans += "D"
    for _ in range(dx + 1): ans += "R"
    for _ in range(dy + 1): ans += "U"
    ans += "L"
    ans += "U"
    for _ in range(dx + 1): ans += "L"
    for _ in range(dy + 1): ans += "D"
    ans += "R"
    print(ans)

    """
    x, y = sx, sy
    for c in ans:
        if c == "U": y += 1
        if c == "D": y -= 1
        if c == "R": x += 1
        if c == "L": x -= 1
        print(x, y)
    """

if __name__ == "__main__":
    main()
