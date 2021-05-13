import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]

    if M < N * 2:
        print(M // 2)
    else:
        ans = N
        M = M - N * 2
        ans += M // 4
        print(ans)
        

if __name__ == '__main__':
    main()

