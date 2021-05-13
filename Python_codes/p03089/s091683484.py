import sys
input = sys.stdin.readline  # NOQA
sys.setrecursionlimit(10 ** 7)  # NOQA


def dfs(N, a, i, procedure):
    if i == 0:
        return procedure

    for j in reversed(range(1, i+1)):
        if a[j-1] == j:
            l = a[:]
            del l[j-1]
            p = procedure[:]
            p.append(j)
            ret = dfs(N, l, i-1, p)
            if ret is not None:
                return ret
            break


def main():
    N = int(input())
    b = list(map(int, input().split()))

    res = dfs(N, b, N, [])
    if res is None:
        print(-1)
    else:
        print(*res[::-1], sep="\n")


if __name__ == "__main__":
    main()
