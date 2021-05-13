import sys

def main():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    diff = [0 for _ in range(N-1)]
    for i in range(N-1):
        diff[i] = X[i+1] - X[i]

    ans = 0
    for d in diff:
        ans += min(A*d, B)

    return ans


if __name__ == '__main__':
    print(main())
