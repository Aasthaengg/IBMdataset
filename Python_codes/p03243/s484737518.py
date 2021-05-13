mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    for i in range(1, 10):
        if i * 111 >= N:
            print(i*111)
            break


if __name__ == '__main__':
    main()
