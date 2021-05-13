def solve():
    N = int(input())
    A = [int(input()) for i in range(N)]

    A = sorted(A)

    i = 0
    k = 0
    ans = 0

    while i < N:
        tmp = A[i]
        n = 0
        while k < N and tmp == A[k]:
            n += 1
            k += 1
        i = k
        if n%2 == 1:
            ans += 1

    print(ans)
            
        


if __name__ == "__main__":
    solve()
