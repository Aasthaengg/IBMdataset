import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n = int(input().rstrip())
    past_max = float("inf")
    ans = 0
    for p in [int(p) for p in input().rstrip().split(" ")]:
        if p < past_max:
            past_max = p
            ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()
