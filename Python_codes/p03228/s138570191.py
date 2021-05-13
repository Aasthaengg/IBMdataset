import sys
readline = sys.stdin.readline


def main():
    abk = list(map(int, input().split()))
    k = abk[2]

    for i in range(k):
        i2 = i % 2
        if abk[i2] % 2 == 1:
            abk[i2] -= 1
        v = abk[i2] // 2
        abk[i2], abk[1 - i2] = abk[i2] - v, abk[1 - i2] + v
    print(abk[0], abk[1])


if __name__ == '__main__':
    main()
