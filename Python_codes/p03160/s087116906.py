import sys

input = sys.stdin.readline


def main():
    N = int(input())
    h = list(map(int, input().split()))

    cost = [0] * N
    cost[1] = abs(h[1] - h[0])
    for i in range(2, N):
        cost_1 = cost[i - 1] + abs(h[i] - h[i - 1])
        cost_2 = cost[i - 2] + abs(h[i] - h[i - 2])
        cost[i] = min(cost_1, cost_2)

    ans = cost[-1]
    print(ans)


if __name__ == "__main__":
    main()
