import math


def resolve():
    import sys
    input = sys.stdin.readline
    a = []
    a1 = [int(x) for x in input().rstrip().split(" ")]
    a2 = [int(x) for x in input().rstrip().split(" ")]
    a3 = [int(x) for x in input().rstrip().split(" ")]


    a += a1 + a2 + a3

    opened = set()

    n = int(input().rstrip())
    for _ in range(n):
        b = int(input().rstrip())
        if b in a:
            opened.add(a.index(b))

    # 判定
    if all([x in opened for x in {0,3,6}]) or all([x in opened for x in {1,4,7}]) or all([x in opened for x in {2,5,8}]):
        print("Yes")
    elif all([x in opened for x in {0,1,2}]) or all([x in opened for x in {3,4,5}]) or all([x in opened for x in {6,7,8}]):
        print("Yes")
    elif all([x in opened for x in {0,4,8}]) or all([x in opened for x in {2,4,6}]):
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    resolve()
