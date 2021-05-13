import sys
input = sys.stdin.readline


def main():
    n = int(input().strip())
    S = input().strip()
    query_table = [0] * (n+1)
    for i, s in enumerate(S):
        if s == "#":
            query_table[i + 1] = query_table[i] + 1
        else:
            query_table[i + 1] = query_table[i]
    ans = float("inf")

    for ptr in range(n+1):
        # left side
        left_black = query_table[ptr]
        left_white = ptr - left_black

        # right side
        right_black = query_table[n] - left_black
        right_white = n - ptr - right_black
        ans = min(ans, left_black+right_white)

    print(ans)

    return


if __name__ == "__main__":
    main()
