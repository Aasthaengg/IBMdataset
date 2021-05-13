import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    n = int(input().rstrip())
    ans = ["" for _ in range(n)]
    a_list = [int(x) for x in input().rstrip().split(" ")]
    for i, a in enumerate(a_list):
        ans[a-1] = str(i+1)

    print(" ".join(ans))



if __name__ == "__main__":
    resolve()
