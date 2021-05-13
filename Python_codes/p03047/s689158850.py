# from itertools import combinations


def main(N, K):
    # nums = [i for i in range(N)]
    # return len(list(combinations(nums, K)))

    return N - K + 1


if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    print(main(N, K))
