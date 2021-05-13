import sys
from itertools import combinations

input = sys.stdin.readline


def main():
    N = int(input())
    S = [""] * N
    for i in range(N):
        S[i] = input().rstrip()

    count = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
    for s in S:
        if s[0] in "MARCH":
            count[s[0]] += 1

    ans = 0
    for c1, c2, c3 in combinations("MARCH", 3):
        ans += count[c1] * count[c2] * count[c3]

    print(ans)


if __name__ == "__main__":
    main()
