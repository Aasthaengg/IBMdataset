def solve():
    N = int(input())
    A1 = [int(i) for i in input().split()]
    A2 = [int(i) for i in input().split()]
    a1 = A1[0]
    a2 = sum(A2)
    ans = a1 + a2
    for i in range(1, N):
        a1 += A1[i]
        a2 -= A2[i - 1]
        ans = max(ans, a1 + a2)
    print(ans)


if __name__ == "__main__":
    solve()
