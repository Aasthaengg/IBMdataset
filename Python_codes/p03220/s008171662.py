# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
import math

def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip())
    t, a = [int(x) for x in input().rstrip().split(" ")]

    min_diff = float('inf')

    for i, h in enumerate(input().rstrip().split(" ")):
        h = int(h)

        temp = t - h * 0.006
        diff = abs(temp - a)
        if min_diff > diff:
            min_diff = diff
            ans = i+1

    print(ans)


if __name__ == "__main__":
    resolve()
