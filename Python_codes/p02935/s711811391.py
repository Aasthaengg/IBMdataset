import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    n = int(input().rstrip())
    v_list = [int(x) for x in input().rstrip().split(" ")]

    v_list.sort()

    ans = v_list[0]
    for i in range(1, len(v_list)):
        ans = (ans + v_list[i]) / 2

    print(ans)



if __name__ == "__main__":
    resolve()
