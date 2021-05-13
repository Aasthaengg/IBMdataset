import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N = input().strip()
    ans = sum([int(n) for n in N])

    for i in range(len(N)-1):
        if N[i] == 0:
            continue
        else:
            ans = max(ans, sum([int(n) for n in N[:i]]) +
                      int(N[i])-1 + 9*(len(N)-i-1))

    return ans


if __name__ == "__main__":
    print(main())