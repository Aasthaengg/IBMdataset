import sys
input = sys.stdin.readline


def main():
    n = int(input())
    A = list(map(int, input().split()))
    flags = [0] * n
    up = False
    prev = 1000
    for i, a in enumerate(A):
        if up:
            if a < prev:
                flags[i-1] = -1
                up = False
        else:
            if a > prev:
                flags[i-1] = 1
                up = True
        prev = a

    money = 1000
    kabu = 0
    for flag, a in zip(flags, A):
        if flag == 1:
            kabu += money // a
            money %= a

        elif flag == -1:
            money += kabu * a
            kabu = 0

    if kabu:
        money += A[-1] * kabu

    print(money)


if __name__ == "__main__":
    main()
