import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    l = list(map(int, input().split()))

    l.sort(reverse=True)
    ans = sum(l[:K])
    print(ans)


if __name__ == "__main__":
    main()
