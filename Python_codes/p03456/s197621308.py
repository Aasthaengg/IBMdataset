import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    ab = int("".join([x for x in input().rstrip().split(" ")]))

    def is_square(n: int):
        return (n ** .5).is_integer()

    if( ab ** .5).is_integer():
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    resolve()
