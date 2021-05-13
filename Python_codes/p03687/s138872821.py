import sys
from string import ascii_lowercase as a2z

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = 100
    for al in a2z:
        if al not in S:
            continue
        i = 0
        max_cost = 0
        for j, s in enumerate(S + al):
            if s == al:
                cost = j - i
                if cost > max_cost:
                    max_cost = cost
                i = j + 1
        if max_cost < ans:
            ans = max_cost

    print(ans)


if __name__ == "__main__":
    main()
