import sys


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())

    num = ["#"] * N

    for _ in range(M):
        # print(num)
        s, c = map(int, sys.stdin.readline().rstrip().split())

        if N > 1 and s == 1 and c == 0:
            break

        if num[s - 1] == "#":
            num[s - 1] = c
            continue

        if num[s - 1] != c:
            break

        # print(num)

    else:

        if N>1 and num[0] == "#":
            num[0] = 1

        for i in range(N):
            if num[i] == "#":
                num[i] = 0

        print("".join(map(str, num)))
        return

    print(-1)
    return


main()
