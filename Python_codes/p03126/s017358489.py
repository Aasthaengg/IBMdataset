import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    ans = [0]*(M+1)
    for _ in range(N):
        food = list(map(int, input().split()))
        K = food[0]
        for i in range(1, K + 1):
            ans[food[i]] += 1
    print(ans.count(N))


if __name__ == '__main__':
    main()
