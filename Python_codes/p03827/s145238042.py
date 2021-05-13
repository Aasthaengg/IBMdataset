import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    S = input()
    ans = 0
    val = 0
    for c in S:
        if c == 'I':
            val += 1
            ans = max(ans, val)
        else:
            val -= 1
    print(ans)


if __name__ == "__main__":
    main()
