import sys
input = sys.stdin.readline


def f(A, n):
    A.sort()
    if A[-1] >= n:
        A[-1] -= n
    else:
        print("No")
        exit()


def main():
    H, W = map(int, input().split())
    import collections
    D = collections.defaultdict(int)
    for _ in range(H):
        s = input().strip()
        for c in s:
            D[c] += 1
    A = list(D.values())

    for i in range(H//2):
        for j in range(W//2):
            f(A, 4)
    if H % 2 == 1:
        for j in range(W//2):
            f(A, 2)
    if W % 2 == 1:
        for i in range(H//2):
            f(A, 2)
    if W % 2 == 1 and H % 2 == 1:
        f(A, 1)

    print("Yes")


if __name__ == '__main__':
    main()
