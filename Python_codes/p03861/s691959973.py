import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    a, b, x = [int(i) for i in input().strip().split()]
    b_x = b // x
    if a > 0:
        a_x = (a - 1) // x
    else:
        a_x = -1
    ans = b_x - a_x
    print(ans)
    return


if __name__ == "__main__":
    main()
