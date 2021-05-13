import sys
input = sys.stdin.readline

def main():
    D, N = [int(x) for x in input().split()]
    if N == 100:
        N += 1
    ans = 100 ** D * N
    print(ans)


if __name__ == '__main__':
    main()



