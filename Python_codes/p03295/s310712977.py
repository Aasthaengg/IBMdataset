import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[0])
    flag = AB[0][1]
    cnt = 1
    for i in range(M):
        if AB[i][0] >= flag:
            flag = AB[i][1]
            cnt += 1
        elif AB[i][1] > flag:
            continue
        else:
            flag = AB[i][1]
    print(cnt)


if __name__ == "__main__":
    main()
