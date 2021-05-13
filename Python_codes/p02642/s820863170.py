def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    D = [True] * (10**6 + 1)
    ans = 0

    for i, a in enumerate(A):
        if not D[a]:
            continue
        if (i < n-1 and a != A[i+1]) or i == n-1:
            ans += 1

        j = a
        while (j < 10**6 + 1):
            D[j] = False
            j += a

    print(ans)


if __name__ == '__main__':
    main()
