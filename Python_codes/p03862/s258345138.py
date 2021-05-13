def solve():
    N, x = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N - 1):
        sumvalue = A[i] + A[i + 1]
        if sumvalue <= x:
            continue
        if i + 1 == N - 1:
            A[i + 1] -= sumvalue - x
        else:
            if A[i + 1] < sumvalue - x:
                A[i] -= sumvalue - x - A[i + 1]
                A[i + 1] = 0
            else:
                A[i + 1] -= sumvalue - x
        ans += sumvalue - x
    print(ans)


if __name__ == "__main__":
    solve()