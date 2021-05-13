import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 1
    n -= k
    ans += (n+k-2) // (k-1)
    print(ans)


if __name__ == "__main__":
    main()