def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    if N == 1:
        return print(1 if A[0] % 2 == 0 else 2)
    ans = 0
    d = (-1, 0, 1)
    from itertools import product
    for i in product(range(3), repeat=N):
        cur = 1
        for j in range(N):
            cur *= (A[j] + d[i[j]])
        if cur % 2 == 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
