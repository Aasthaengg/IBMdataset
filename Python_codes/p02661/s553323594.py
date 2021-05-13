import sys
input = sys.stdin.readline


def main():
    n = int(input())
    A, B = [], []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    if n % 2 == 1:
        left = A[n // 2]
        right = B[n // 2]
    else:
        m = n // 2 - 1
        left = A[m] + A[m + 1]
        right = B[m] + B[m + 1]

    ans = right - left + 1
    print(ans)

if __name__ == '__main__':
    main()