import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n, 0, -1):
        s = 0
        for j in range(i, n + 1, i):
            s += ans[j - 1]
        if s % 2 == a[i - 1]:
            ans[i - 1] = 0
        else:
            ans[i - 1] = 1
    m = sum(ans)
    print(m)
    for i in range(1, n + 1):
        if ans[i - 1]:
            print(i)


if __name__ == "__main__":
    main()
