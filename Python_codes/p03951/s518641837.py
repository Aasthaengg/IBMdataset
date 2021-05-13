import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().strip()
    T = input().strip()

    x = 0
    for i in range(N):
        if S[i:] == T[:N - i]:
            x = N - i
            break

    print(N * 2 - x)


    

if __name__ == '__main__':
    main()

