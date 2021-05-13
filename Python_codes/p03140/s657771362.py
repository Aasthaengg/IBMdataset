import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = input().rstrip()
    B = input().rstrip()
    C = input().rstrip()

    ans = 0
    for a, b, c in zip(A, B, C):
        if a == b == c:
            pass
        elif a == b or b == c or c == a:
            ans += 1
        else:
            ans += 2

    print(ans)


if __name__ == "__main__":
    main()
