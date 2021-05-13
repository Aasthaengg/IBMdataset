import sys
def input(): return sys.stdin.readline().strip()


def main():
    n, a, b = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        s = str(i)
        val = 0
        for c in s:
            val += int(c)
        if a <= val <= b:
            ans += i
    print(ans)


if __name__ == "__main__":
    main()
