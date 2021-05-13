import sys
from itertools import product

input = sys.stdin.readline


def main():
    N = int(input())

    ans = []
    if N % 2 == 0:
        groups = [(1 + i, N - i) for i in range(N // 2)]
    else:
        groups = [(1 + i, N - 1 - i) for i in range((N - 1) // 2)] + [(N,)]

    for i in range(len(groups) - 1):
        group_a = groups[i]
        group_b = groups[i + 1]
        for a, b in product(group_a, group_b):
            ans.append(f"{a} {b}")

    if len(groups) >= 3:
        group_a = groups[0]
        group_b = groups[-1]
        for a, b in product(group_a, group_b):
            ans.append(f"{a} {b}")

    print(len(ans))
    print("\n".join(ans))


if __name__ == "__main__":
    main()
