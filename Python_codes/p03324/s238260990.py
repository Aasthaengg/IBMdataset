def main():
    import sys
    input = sys.stdin.readline
    D, N = map(int, input().split())
    if N != 100:
        print(N, end="")
        for i in range(D):
            print("00", end="")
        print("")
    else:
        print(100 ** (D+1) + 100 ** D)

if __name__ == '__main__':
    main()