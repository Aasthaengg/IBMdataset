mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    S = input().rstrip('\n')
    K = int(input())

    for i in range(K-1):
        if S[i] != "1":
            print(S[i])
            exit()
    print(S[K-1])


if __name__ == '__main__':
    main()
