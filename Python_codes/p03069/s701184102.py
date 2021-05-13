import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    n = int(input())
    s = input()
    w = s.count(".")
    b = n - w
    ans = min(w, b)
    b = 0
    for i in range(n):
        if s[i] == ".":
            w -= 1
        else:
            b += 1
        ans = min(ans, w + b)
    print(ans)


if __name__ == '__main__':
    main()
