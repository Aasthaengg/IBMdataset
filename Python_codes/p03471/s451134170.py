# vim: fileencoding=utf-8


def main():
    n, y = map(int, input().split())
    maxA = min(n, y // 10000)
    maxB = min(n, y // 5000)
    for i in range(maxA, -1, -1):
        t = y - 10000 * i
        if t == 0:
            if n == i:
                print(f"{i} 0 0")
                return
            continue
        for j in range(min(maxB, n - i), -1, -1):
            tt = t
            tt -= 5000 * j
            if tt == 0:
                if n == i + j:
                    print(f"{i} {j} 0")
                    return
            if tt > 0 and tt == (n - (i + j)) * 1000:
                print(f"{i} {j} {n-(i+j)}")
                return
    print("-1 -1 -1")


if __name__ == "__main__":
    main()
