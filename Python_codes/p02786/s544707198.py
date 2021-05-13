import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    h = int(input().rstrip())

    def process(num: int):
        if num == 1:
            return 1
        else:
            count = 2 * process(num // 2)+1

        return count

    print(process(h))



if __name__ == "__main__":
    resolve()
