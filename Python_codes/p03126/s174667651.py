import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    like_food = [0] * M
    for _ in range(N):
        _, *A = map(int, input().split())
        for a in A:
            like_food[a - 1] += 1

    ans = like_food.count(N)
    print(ans)


if __name__ == "__main__":
    main()
