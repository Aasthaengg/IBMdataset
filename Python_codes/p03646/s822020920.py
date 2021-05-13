import sys

def f(A):
    n = len(A)
    A = sorted(A)
    B = [A[0] + n]
    for a in A[1:]:
        B.append(a-1)

    return B


def main():
    input = sys.stdin.readline
    K = int(input())

    i = 2
    while i <= 50:
        n = K // i
        m = K % i

        A = [0 for _ in range(i)]
        for j in range(i):
            A[j] = n + j

        for _ in range(m):
            A = f(A)

        if max(A) <= 10**16 + 1000:
            print(i)
            print(*A)
            return 0
        else:
            i += 1


if __name__ == '__main__':
    main()
