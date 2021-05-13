import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]
    ans = 0
    for i in range(N):
        val = sum(A[0][:i + 1]) + sum(A[1][i:])
        ans = max(ans, val)
    print(ans)


if __name__ == "__main__":
    main()
