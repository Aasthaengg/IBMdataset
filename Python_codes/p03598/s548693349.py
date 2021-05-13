import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    n = int(input().rstrip())
    k = int(input().rstrip())
    x_list = [int(x) for x in input().rstrip().split(" ")]

    distance = 0
    for x in x_list:
        distance += (x if x < abs(k-x) else abs(k-x)) * 2


    print(distance)

if __name__ == "__main__":
    resolve()
