import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    n = int(input().rstrip())
    a_list = [int(x) for x in input().rstrip().split(" ")]
    a_list.sort(reverse=True)

    alice = 0
    bob = 0
    for i in range(len(a_list)):
        if i % 2 == 0:
            alice += a_list[i]
        else:
            bob += a_list[i]
    print(alice-bob)

if __name__ == "__main__":
    resolve()
