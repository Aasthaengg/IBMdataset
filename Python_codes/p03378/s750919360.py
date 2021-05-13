import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    nmx = [int(x) for x in input().rstrip().split(" ")]
    x = nmx[2]
    a_list = [int(x) for x in input().rstrip().split(" ")]


    left_cost = sum(1 for a in a_list if a < x)
    right_cost = len(a_list) - left_cost

    ans = left_cost if left_cost < right_cost else right_cost

    print(ans)




if __name__ == "__main__":
    resolve()
