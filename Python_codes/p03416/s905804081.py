import sys

input = sys.stdin.readline


def is_palindromic(s):
    if s[0] == s[-1] and s[1] == s[-2]:
        return True
    else:
        return False


def main():
    A, B = map(int, input().split())

    ans = 0
    for i in range(A, B + 1):
        ans += 1 if is_palindromic(str(i)) else 0

    print(ans)


if __name__ == "__main__":
    main()
