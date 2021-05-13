def main():
    n = int(input())
    A = list(map(int, input().split()))
    A += A
    ans = [0] * n
    s1 = sum(A[:n - 1:2])
    s2 = sum(A[1:n:2])
    for i in range(n):
        if i % 2 == 0:
            s1 += A[i + n - 1]
            ans[i] = s1 - s2
            s1 -= A[i]
        else:
            s2 += A[i + n - 1]
            ans[i] = s2 - s1
            s2 -= A[i]
    print(' '.join(list(map(str, ans))))

if __name__ == '__main__':
    main()
