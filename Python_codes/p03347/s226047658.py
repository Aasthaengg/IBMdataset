import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    if A[0] != 0:
        print(-1)
        return

    ans = 0
    for a, b in zip(A[0:], A[1:]):
        if b - a >= 2:
            print(-1)
            return
        elif b - a == 1 or (a == 1 and a == b):
            ans += 1
        else:
            ans += b

    print(ans)




if __name__ == '__main__':
    main()
