import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    A.sort()
    ans = 0
    for i in range(N, 3 * N, 2):
        ans += A[i]

    print(ans)


    

if __name__ == '__main__':
    main()

