import math


def resolve():
    import sys
    input = sys.stdin.readline
    row = [int(x) for x in input().rstrip().split(" ")]
    a = row[0]
    b = row[1]

    x = (b-1) / (a-1)
    print(math.ceil(x))




if __name__ == "__main__":
    resolve()
