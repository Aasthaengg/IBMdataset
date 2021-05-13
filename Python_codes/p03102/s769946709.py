import math


def resolve():
    import sys
    input = sys.stdin.readline
    row1 = [int(x) for x in input().rstrip().split(" ")]
    n = row1[0]
    c = row1[2]

    ans = 0
    b_list = [int(x) for x in input().rstrip().split(" ")]
    for _ in range(n):
        a_list = [int(x) for x in input().rstrip().split(" ")]

        if sum([a*b for a, b in zip(a_list, b_list)]) + c > 0:
            ans += 1

    print(ans)





if __name__ == "__main__":
    resolve()
