# ARC100C - Linear Approximation (ABC102C)
def main():
    n = int(input())
    A = tuple(map(int, input().rstrip().split()))
    A = sorted(j - i for i, j in enumerate(A, start=1))
    b = A[n // 2]
    ans = sum(abs(a - b) for a in A)
    print(ans)


if __name__ == "__main__":
    main()