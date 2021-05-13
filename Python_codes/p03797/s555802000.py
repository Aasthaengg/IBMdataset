import math


def main():
    N, M = list(map(int, input().split(' ')))
    if N >= M // 2:
        print(M // 2)
    else:
        t = math.ceil(((M // 2) - N) / 2)
        print((M - 2 * t) // 2)



if __name__ == '__main__':
    main()