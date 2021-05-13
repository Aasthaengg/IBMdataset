import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    a = list(map(int, input().split()))
    A = [0] + a
    B = [0] * (N + 1)

    for i in range(N, 0, -1):
        j = 2
        count = 0
        while i * j <= N:
            count += B[i * j]
            j += 1
        if (count + A[i]) % 2 == 0:
            pass
        else:
            B[i] = 1
    print(sum(B))

    for i in range(len(B)):
        if B[i]==1:
            print(i,end=" ")

if __name__ == "__main__":
    main()
