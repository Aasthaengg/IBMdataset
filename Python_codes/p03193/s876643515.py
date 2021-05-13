import sys

input = sys.stdin.readline


def main():
    N, H, W = map(int, input().split())
    ans = 0
    for _ in range(N):
        A, B = map(int, input().split())
        if H <= A and W <= B:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
