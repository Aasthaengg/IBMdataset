def main():
    N = int(input())
    A = list(map(int, input().split()))
    a = sum(A) / len(A)
    f, m = 0, abs(A[0] - a)
    for i, j in enumerate(A[1:], 1):
        t = abs(j - a)
        if t < m:
            f, m = i, t
    print(f)

main()
