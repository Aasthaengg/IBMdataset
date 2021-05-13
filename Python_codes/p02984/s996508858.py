import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    tmp = 0
    ans = [0] * n
    f = 1
    for i in a:
        tmp += f * i
        f = f * -1
    ans[0] = tmp
    ans[n - 1] = 2 * a[n - 1] - ans[0]
    for i in range(n - 2, 0, -1):
        ans[i] = 2 * a[i] - ans[i + 1]

    print(" ".join([str(i) for i in ans]))


if __name__ == "__main__":
    main()
