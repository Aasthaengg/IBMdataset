import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    if N==1:
        print(input())
        exit()
    h = list(map(int, input().split()))


    dflag = 0
    cmin = 0
    cmax = h[0]
    count = 0
    for i in range(1, N):
        if h[i - 1] < h[i] and dflag == 1:
            count += cmax - cmin
            cmax = h[i]
            dflag = 0
            cmin = h[i - 1]

        elif h[i - 1] > h[i]:
            dflag = 1

        elif h[i - 1] < h[i]:
            cmax = h[i]

    if dflag == 1:
        count += cmax - cmin
    else:
        count += max(cmax, h[i]) - cmin

    print(count)


if __name__ == "__main__":
    main()
