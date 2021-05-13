import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append((a+b, a, b))
    A.sort(reverse=True)
    takahashi = aoki = 0
    for i, (_, a, b) in enumerate(A):
        if i % 2 == 0:
            takahashi += a
        else:
            aoki += b
    print(takahashi - aoki)


if __name__ == '__main__':
    main()
