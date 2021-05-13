from itertools import combinations as comb


def main():
    abc = list(map(int, input().split()))
    abc_pairs = comb(abc, 2)
    ans = float("inf")

    for abc_pair in abc_pairs:
        ans = min(ans, sum(abc_pair))

    print(ans)


if __name__ == "__main__":
    main()
