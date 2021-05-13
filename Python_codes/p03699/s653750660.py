import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]
    S.sort()
    ans = sum(S)
    if ans % 10 != 0:
        print(ans)
        return
    subtract = 0
    for s in S:
        if s % 10 != 0:
            subtract = s
            break
    if subtract != 0:
        print(ans - subtract)
    else:
        print(0)


if __name__ == "__main__":
    main()
