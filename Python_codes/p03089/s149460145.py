import sys


def input():
    return sys.stdin.readline().strip()
# sys.setrecursionlimit(100000)


def main():
    n = int(input().strip())
    B = [int(i) for i in input().strip().split()]
    ans = []
    ptr = len(B)
    while ptr > 0:
        if B[ptr - 1] == ptr:
            ans.append(B.pop(ptr - 1))
            ptr = len(B)
        else:
            ptr -= 1
    if len(ans) == n:
        for i in ans[::-1]:
            print(i)
    else:
        print(-1)

    return


if __name__ == "__main__":
    main()
