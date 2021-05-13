import sys
def input(): return sys.stdin.readline().strip()


def main():
    L = list(map(int, input().split()))
    L.sort()
    a, b, c = L[0], L[1], L[2]
    ans = c - b
    a += ans
    if (c - a) % 2 != 0:
        ans += 1
        c += 1
    print(ans + (c - a) // 2)


if __name__ == "__main__":
    main()
